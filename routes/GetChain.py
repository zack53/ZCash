from flask_server import app, blockchain
from flask import Flask, request

@app.route('/get_chain', methods = ['GET'])
def get_chain():
    respone = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain)
    }
    return respone