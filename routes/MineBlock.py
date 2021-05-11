from flask_server import app, blockchain
from flask import Flask, request

@app.route('/mine_block', methods = ['GET'])
def mine_block():
    previous_block = blockchain.getPreviousBlock()
    previous_proof = previous_block['proof']
    proof = blockchain.proofOfWork(previous_proof)
    block = blockchain.create_block(proof,blockchain.hashFunction(previous_block))
    response = {
        'message' : 'Congratulations you just mined a block!',
        'index' : block['index'],
        'timestamp' : block['timestamp'],
        'proof' : block['proof'],
        'previous_hash' : block['previous_hash']
    }
    return response