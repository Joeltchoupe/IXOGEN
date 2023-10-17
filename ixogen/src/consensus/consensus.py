
MAX_BLOCK_SERIALIZED_SIZE = 4000000
MAX_BLOCK_WEIGHT = 4000000
MAX_BLOCK_SIGOPS_COST = 80000
COINBASE_MATURITY = 100
WITNESS_SCALE_FACTOR = 4
MIN_TRANSACTION_WEIGHT = WITNESS_SCALE_FACTOR * 60
MIN_SERIALIZABLE_TRANSACTION_WEIGHT = WITNESS_SCALE_FACTOR * 10

LOCKTIME_VERIFY_SEQUENCE = (1 << 0)