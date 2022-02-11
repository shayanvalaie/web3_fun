from connect_with_eth import Web3


"Connect "

infura_url = ""
web3 = Web3(Web3.HTTPProvider(infura_url))
print(web3.isConnected())

print(web3.eth.blockNumber)
balance = web3.eth.getBalance("meta_mask_id")
print(balance)
