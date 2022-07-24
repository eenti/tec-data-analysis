import time
from web3 import Web3

web3 = Web3(Web3.HTTPProvider('https://rpc.gnosischain.com'))
web3.isConnected()

block = web3.eth.get_transaction('0xdff6daa7178d6c0afbeaf7b865846ead0d0bffa0f85fc2e0225ae32cc70507e5')
block_seconds = (web3.eth.get_block(block['blockNumber'])['timestamp'])
block_datetime = time.strftime('%Y-%m-%d', time.localtime(block_seconds))

print(block_datetime)