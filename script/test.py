import sys
import os
import web3
import numpy as np
import pandas as pd
from web3 import Web3
import time
import json
from eth_account.messages import encode_defunct, _hash_eip191_message

import pandas as pd

url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(url))
print(web3.isConnected())
#print(web3.eth.getBlock('latest'))
#print(web3.eth.coinbase)

#address
proxy_addr = "0x7565B6Bcaa94d52Ac4C2B700B3d0B15e4bDb5106"
tokenState_addr = "0x63bec50139b822C0F244785cF39Ff53e79b87626"
externStateToken_addr = "0x18F293D8958DBadD8dE3460E7cEabb2035Bbfa50"


#abi
f = open('./build/contracts/ProxyERC20.json', "r") 
proxy_abi = json.load(f)['abi']
f.close()

f = open('./build/contracts/TokenState.json', "r") 
tokenState_abi = json.load(f)['abi']
f.close()


f = open('./build/contracts/PublicEST.json', "r") 
externStateToken_abi = json.load(f)['abi']
f.close()

#
owner = web3.eth.accounts[0]
web3.eth.defaultAccount = web3.eth.accounts[0]
web3.geth.personal.unlockAccount(web3.eth.defaultAccount,'',0)


# Contract Instance
proxyInstance = web3.eth.contract(address=proxy_addr, abi=proxy_abi)
tokenStateInstance = web3.eth.contract(address=tokenState_addr, abi=tokenState_abi)
externStateTokenInstance = web3.eth.contract(address=externStateToken_addr, abi=externStateToken_abi)

#1. tokenState.setBalanceOf(owner, totalSupply)
# totalSupply = 100000000
# tx_hash = tokenStateInstance.functions.setBalanceOf(owner,totalSupply).transact()
# receipt = web3.eth.waitForTransactionReceipt(tx_hash)
# print(receipt)


#2. tokenState.setAssociatedContract(token.address, { from: owner })
# tx_hash = tokenStateInstance.functions.setAssociatedContract(externStateToken_addr).transact()
# receipt = web3.eth.waitForTransactionReceipt(tx_hash)
# print(receipt)	

#3. proxy.setTarget(token.address, { from: owner })
# tx_hash = proxyInstance.functions.setTarget(externStateToken_addr).transact()
# receipt = web3.eth.waitForTransactionReceipt(tx_hash)
# print(receipt)	
# curr_name = proxyInstance.functions.name().call()
# print(curr_name)
# curr_decimal = proxyInstance.functions.decimals().call()
# print(curr_decimal)
# curr_total = proxyInstance.functions.totalSupply().call()
# print(curr_total)

#4. do a transfer   token.transfer
receiver = web3.eth.accounts[1]
# print(externStateTokenInstance.functions.balanceOf(owner).call())
# tx_hash = externStateTokenInstance.functions.transfer(receiver, 10000).transact().hex()
# receipt = web3.eth.waitForTransactionReceipt(tx_hash)
# print("Transfer")
# print(receipt)
print("balance result: [owner, receiver]")
print(proxyInstance.functions.balanceOf(owner).call())
print(proxyInstance.functions.balanceOf(receiver).call())
tx_hash = proxyInstance.functions.transfer(receiver, 10000).transact().hex()
receipt = web3.eth.waitForTransactionReceipt(tx_hash)
print("proxy transfer")
print("balance result: [owner, receiver]")
print(proxyInstance.functions.balanceOf(owner).call())
print(proxyInstance.functions.balanceOf(receiver).call())




