from web3 import Web3
from hexbytes import HexBytes
from eth_typing.encoding import HexStr
class Web3Utils:
    def __init__(self) -> None:
        pass

    def to_int(self, hex: HexBytes) -> int:
        return Web3.toInt(Web3.toBytes(primitive=hex))
    