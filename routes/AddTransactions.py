from flask_server import app, blockchain
from flask import request

@app.route('/add_transaction', methods = ['POST'])
def add_transaction():
    json = request.get_json()
    transaction_keys = ['sender', 'receiver', 'amount']
    if not all (key in json for key in transaction_keys):
        return 'Some elements of the transaction are missing.', 400
    index = blockchain.addTransaction(json['sender'], json['receiver'], json['amount'])
    response = {
        'message' : 'This transaction will be added to block '+ str(index)
    }
    return response, 201