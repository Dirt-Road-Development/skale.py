import web3

def test_case_1():
    w3 = web3.Web3(web3.HTTPProvider("http://staging-v3.skalenodes.com/v1/staging-utter-unripe-menkar"))
    w3.eth.account.from_key("<private-key>")
    
    print(w3.eth.send_transaction({
        'from': '0xD99c39BB76D284D21FDEB1364Ae3F1d6F6874050',
        'to': "0x28eF74Ddc12e04054b52E48b161EbE957c21BFD7",
        'value': web3.Web3.toWei(0.00000001, "ether")
    }))
    assert True is False

    # signed_tx = self.web3.eth.account.sign_transaction(tx, self.private_key)
    #     print("Chain Id: ", self.web3.eth.chain_id)
    #     print("Signed Tx: ", signed_tx)
    #     tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    #     print("Tx Hash: ", tx_hash.hex())
    #     receipt = self.web3.eth.wait_for_transaction_receipt(tx_hash)
    #     print("Receipt", receipt)
    #     return tx_hash.hex()