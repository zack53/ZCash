from flask_server import app, blockchain
from flask import Flask, request

@app.route('/getPreviousBlock', methods = ['GET'])
def GetPreviousBlock():
    return blockchain.getPreviousBlock()