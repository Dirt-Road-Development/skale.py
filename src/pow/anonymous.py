from pow.wallet import WalletPow
from secrets import token_hex
from eth_keys import datatypes

class AnonymousPow(WalletPow):
    def __init__(self, rpc_url: str, difficulty=None) -> None:
        private_key = "0x" + token_hex(32)
        super().__init__(private_key, rpc_url, difficulty)