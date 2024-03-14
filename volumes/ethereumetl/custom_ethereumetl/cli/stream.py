import logging

from blockchainetl.streaming.streaming_utils import configure_signals, configure_logging

from ethereumetl.cli.stream import parse_entity_types
from ethereumetl.providers.auto import get_provider_from_uri
from ethereumetl.streaming.item_exporter_creator import create_item_exporters
from ethereumetl.thread_local_proxy import ThreadLocalProxy

def stream(last_synced_block_file, provider_uri, entity_types, 
           start_block=None, output=None,  log_file=None, pid_file=None,
           lag=0, period_seconds=10, batch_size=2, block_batch_size=10, max_workers=5):
    """Streams all data types to console or Google Pub/Sub."""

    configure_logging(log_file)
    configure_signals()
    entity_types = parse_entity_types(entity_types)

    from custom_blockchainetl.streaming.streamer import Streamer
    from custom_ethereumetl.streaming.eth_streamer_adapter import EthStreamerAdapter

    logging.info('Using ' + provider_uri)

    streamer_adapter = EthStreamerAdapter(
        batch_web3_provider=ThreadLocalProxy(lambda: get_provider_from_uri(provider_uri, batch=True)),
        item_exporter=create_item_exporters(output),
        batch_size=batch_size,
        max_workers=max_workers,
        entity_types=entity_types
    )
    streamer = Streamer(
        blockchain_streamer_adapter=streamer_adapter,
        last_synced_block_file=last_synced_block_file,
        lag=lag,
        start_block=start_block,
        period_seconds=period_seconds,
        block_batch_size=block_batch_size,
        pid_file=pid_file
    )
    streamer.stream()