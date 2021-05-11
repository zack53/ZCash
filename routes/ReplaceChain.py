from CryptoCurrency.ZCash import ZCash
from flask_server import app, blockchain
from flask import Flask, request

@app.route('/replace_chain', methods = ['GET'])
def replace_chain():
    isChainReplaced = blockchain.replace_chain(blockchain.chain)
    if isChainReplaced:
        response = {
                'message' : 'The node had a different chains so the chain was replaced with the longest.',
                'new_chain' : blockchain.chain
            } 
    else:
        response = {
                'message' : 'The node had the longest chain so the chain was not replaced.',
                'actual_chain' : blockchain.chain    
            } 
    return response