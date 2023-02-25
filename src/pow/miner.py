from eth_utils.hexadecimal import is_hex
from web3 import Web3
from utils.web3_utils import Web3Utils
from secrets import token_bytes
from eth_typing.encoding import HexStr

class SkalePowMiner:

    utils = Web3Utils()

    def __init__(self, difficulty = None) -> None:
        if difficulty is None:
            self.difficulty = 1
        else:
            self.difficulty = difficulty
        pass

    def mineFreeGas(self, gas: int, from_address: str, nonce: int, randomBytes = None) -> str:
        nonce_hash = int(Web3.solidityKeccak(['uint256'], [nonce]).hex(), 16)
        address_hash = int(Web3.solidityKeccak(['address'], [from_address]).hex(), 16)
        nonce_address_XOR = nonce_hash ^ address_hash
        max_number = pow(2, 256) - 1
        div_constant = max_number / self.difficulty
        candidate = None
        while True:
            candidate = token_bytes(32).hex() if (randomBytes is None) else randomBytes
            candidate_hash = int(Web3.solidityKeccak(['uint256'], [int(candidate, base=16)]).hex(), 16)
            result_hash = nonce_address_XOR ^ candidate_hash
            external_gas = div_constant / result_hash
            if external_gas >= gas:
                break
        return candidate