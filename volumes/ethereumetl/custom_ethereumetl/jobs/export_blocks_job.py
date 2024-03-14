import ethereumetl.jobs.export_blocks_job as export_blocks_job

from custom_ethereumetl.mappers.block_mapper import EthBlockMapper
from ethereumetl.executors.batch_work_executor import BatchWorkExecutor
from ethereumetl.mappers.transaction_mapper import EthTransactionMapper
from ethereumetl.utils import validate_range

class ExportBlocksJob(export_blocks_job.ExportBlocksJob):
    def __init__(
            self,
            start_block,
            end_block,
            batch_size,
            batch_web3_provider,
            max_workers,
            item_exporter,
            export_blocks=True,
            export_transactions=True):
        validate_range(start_block, end_block)
        self.start_block = start_block
        self.end_block = end_block

        self.batch_web3_provider = batch_web3_provider

        self.batch_work_executor = BatchWorkExecutor(batch_size, max_workers)
        self.item_exporter = item_exporter

        self.export_blocks = export_blocks
        self.export_transactions = export_transactions
        if not self.export_blocks and not self.export_transactions:
            raise ValueError('At least one of export_blocks or export_transactions must be True')

        self.block_mapper = EthBlockMapper()
        self.transaction_mapper = EthTransactionMapper()