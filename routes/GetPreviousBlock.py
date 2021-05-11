from flask_server import app, blockchain

@app.route('/getPreviousBlock', methods = ['GET'])
def GetPreviousBlock():
    return blockchain.getPreviousBlock()