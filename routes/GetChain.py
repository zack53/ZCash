from flask_server import app, blockchain

@app.route('/get_chain', methods = ['GET'])
def get_chain():
    respone = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain)
    }
    return respone