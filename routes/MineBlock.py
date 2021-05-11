from flask_server import app, blockchain, nodeAddress
from flask import request
from urllib.parse import urlparse, parse_qs

@app.route('/mine_block', methods = ['GET'])
def mine_block():
    parsedURL = urlparse(request.url)
    if 'miner' not in parse_qs(parsedURL.query):
        return {'message' : "Please include the ?miner query paramter onto your string passing in the miner's details"}
    minerUser = parse_qs(parsedURL.query)['miner']
    previous_block = blockchain.getPreviousBlock()
    previous_proof = previous_block['proof']
    proof = blockchain.proofOfWork(previous_proof)
    blockchain.addTransaction(nodeAddress, minerUser, 1)
    block = blockchain.create_block(proof,blockchain.hashFunction(previous_block))
    response = {
        'message' : 'Congratulations you just mined a block!',
        'index' : block['index'],
        'timestamp' : block['timestamp'],
        'proof' : block['proof'],
        'previous_hash' : block['previous_hash'],
        'transactions' : block['transactions']
    }
    return response