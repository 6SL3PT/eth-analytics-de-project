import ethereumetl.mappers.block_mapper as eth_block_mapper

from ethereumetl.mappers.transaction_mapper import EthTransactionMapper

class EthBlockMapper(eth_block_mapper.EthBlockMapper):
    def __init__(self, transaction_mapper=None):
        if transaction_mapper is None:
            self.transaction_mapper = EthTransactionMapper()
        else:
            self.transaction_mapper = transaction_mapper
    
    def _sum_array(self, arr) -> int:
        sum = 0
        for i in arr: sum += i

        return sum
    
    def block_to_dict(self, block):
        return {
            'type': 'block',
            'number': block.number,
            'hash': block.hash,
            # 'parent_hash': block.parent_hash,
            # 'nonce': block.nonce,
            # 'sha3_uncles': block.sha3_uncles,
            # 'logs_bloom': block.logs_bloom,
            # 'transactions_root': block.transactions_root,
            # 'state_root': block.state_root,
            # 'receipts_root': block.receipts_root,
            # 'miner': block.miner,
            # 'difficulty': block.difficulty,
            # 'total_difficulty': block.total_difficulty,
            'size': block.size,
            # 'extra_data': block.extra_data,
            'gas_limit': block.gas_limit,
            'gas_used': block.gas_used,
            'block_timestamp': block.timestamp,
            'transaction_count': block.transaction_count,
            'base_fee_per_gas': block.base_fee_per_gas,
            # 'withdrawals_root': block.withdrawals_root,
            'withdrawals_amount': self._sum_array([int(w['amount']) for w in block.withdrawals]),
        }