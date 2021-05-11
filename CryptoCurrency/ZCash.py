import sys
import os
sys.path.append(os.path.abspath('../BlockchainModule'))
from Blockchain import Blockchain
import requests
from uuid import uuid4
from urllib.parse import urlparse

#Module 2 - Create a Cryptocurrency

class ZCash(Blockchain):
    
    def __init__(self):
        Blockchain.__init__(self)

    def addTransaction(self, sender, receiver, amount):
        self.transactions.append({
            'sender' : sender, 
            'receiver' : receiver, 
            'amount' : amount
            })
        previous_block = self.getPreviousBlock()
        return previous_block['index'] + 1

cash = ZCash()
print(cash.addTransaction('test','user',100))
print(cash.transactions)