from pow.miner import SkalePowMiner
from web3 import Web3, HTTPProvider, Account
from eth_typing.encoding import HexStr

class WalletPow(SkalePowMiner):
    from_address: str
    private_key: str
    web3: Web3

    def __init__(self, private_key: str, rpc_url: str, difficulty = None) -> None:
        self.difficulty = difficulty
        self.private_key = private_key
        self.web3 = Web3(HTTPProvider(rpc_url))
        self.from_address = self.web3.eth.account.from_key(self.private_key).address
        print("Block Num: ", self.web3.eth.get_block_number)
        super().__init__(difficulty)

    def send(self, to: str, data, randomBytes = None, gas: int = 100000):
        nonce = self.web3.eth.get_transaction_count(to)
        gas_hash = self.mineFreeGas(gas, self.from_address, nonce, randomBytes)
        tx = {
            'from': self.from_address,
            'nonce': nonce,
            'to': to,
            'data': data,
            'gas': gas,
            'gasPrice': int(gas_hash, 16),
            'chainId': self.web3.eth.chain_id   
        }
        print("Web3: ", self.web3.isConnected())
        signed_tx = self.web3.eth.account.sign_transaction(tx, self.private_key)
        print("Chain Id: ", self.web3.eth.chain_id)
        print("Signed Tx: ", signed_tx)
        tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        print("Tx Hash: ", tx_hash.hex())
        receipt = self.web3.eth.wait_for_transaction_receipt(tx_hash)
        print("Receipt", receipt)
        return tx_hash.hex()