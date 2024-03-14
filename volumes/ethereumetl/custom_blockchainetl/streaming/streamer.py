import blockchainetl.streaming.streamer as blockchain_streamer
import logging
import os
import time

from blockchainetl.streaming.streamer import (
    init_last_synced_block_file, read_last_synced_block, write_to_file, 
    delete_file, write_last_synced_block
)
from blockchainetl.streaming.streamer_adapter_stub import StreamerAdapterStub
from requests.exceptions import HTTPError

class Streamer(blockchain_streamer.Streamer):
    def __init__(
            self,
            blockchain_streamer_adapter=StreamerAdapterStub(),
            last_synced_block_file='last_synced_block.txt',
            lag=0,
            start_block=None,
            end_block=None,
            period_seconds=10,
            block_batch_size=10,
            retry_errors=True,
            pid_file=None):
        self.blockchain_streamer_adapter = blockchain_streamer_adapter
        self.last_synced_block_file = last_synced_block_file
        self.lag = lag
        self.start_block = start_block
        self.end_block = end_block
        self.period_seconds = period_seconds
        self.block_batch_size = block_batch_size
        self.retry_errors = retry_errors
        self.pid_file = pid_file

        if self.start_block is not None or not os.path.isfile(self.last_synced_block_file):
            init_last_synced_block_file((self.start_block or 0) - 1, self.last_synced_block_file)

        self.last_synced_block = read_last_synced_block(self.last_synced_block_file)
    
    def stream(self):
        try:
            if self.pid_file is not None:
                logging.info('Creating pid file {}'.format(self.pid_file))
                write_to_file(self.pid_file, str(os.getpid()))
            self.blockchain_streamer_adapter.open()
            self._do_stream()
        finally:
            self.blockchain_streamer_adapter.close()
            if self.pid_file is not None:
                logging.info('Deleting pid file {}'.format(self.pid_file))
                delete_file(self.pid_file)

    def _do_stream(self):
        while True and (self.end_block is None or self.last_synced_block < self.end_block):
            synced_blocks = 0

            try:
                synced_blocks = self._sync_cycle()
            except HTTPError as e:
                logging.exception('An exception occurred while syncing block data.')
                if e.response.status_code >= 400:
                    raise e
            except Exception as e:
                logging.exception('An exception occurred while syncing block data.')
                if not self.retry_errors:   
                    raise e
            
            time.sleep(self.period_seconds)
            # if synced_blocks <= 0:
            #     logging.info('Nothing to sync. Sleeping for {} seconds...'.format(self.period_seconds))
            #     time.sleep(self.period_seconds)

    def _sync_cycle(self):
        current_block = self.blockchain_streamer_adapter.get_current_block_number()

        target_block = self._calculate_target_block(current_block, self.last_synced_block)
        blocks_to_sync = max(target_block - self.last_synced_block, 0)

        logging.info('Current block {}, target block {}, last synced block {}, blocks to sync {}'.format(
            current_block, target_block, self.last_synced_block, blocks_to_sync))

        if blocks_to_sync != 0:
            self.blockchain_streamer_adapter.export_all(self.last_synced_block + 1, target_block)
            logging.info('Writing last synced block {}'.format(target_block))
            write_last_synced_block(self.last_synced_block_file, target_block)
            self.last_synced_block = target_block

        return blocks_to_sync
