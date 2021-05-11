from flask_server import app, blockchain

@app.route('/is_valid', methods = ['GET'])
def is_valid():
    respone = {
        'isChainValid': blockchain.isChainValid(blockchain.chain)
    }
    return respone