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

    def add_node(self, address):
        parsed_url = urlparse(address)
        self.nodes.add(parsed_url.netloc)

    def replace_chain(self):
        network = self.nodes
        longest_chain = None
        max_length = len(self.chain)
        for node in network:
            response = requests.get('http://'+node+'/get_chain')
            if response.status_code == 200:
                length = int(response.json()['length'])
                chain = response.json()['chain']
                if length > max_length and self.isChainValid(chain):
                    max_length = length 
                    longest_chain = chain
        if longest_chain:
            self.chain = longest_chain
            return True
        return False
cash = ZCash()
print(cash.addTransaction('test','user',100))
print(cash.transactions)