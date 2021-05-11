from flask_server import app, blockchain
from flask import request

@app.route('/connect_node', methods = ['POST'])
def connect_node():
    json = request.get_json()
    nodes = json.get('nodes')
    if nodes is None:
        return 'No node', 400
    for node in nodes:
        blockchain.add_node(node)
    response = {
        'message' : 'All the nodes are now connected. The ZCash Blockchain now contains the following nodes:',
        'total_nodes' : list(blockchain.nodes)
    }
    return response, 201