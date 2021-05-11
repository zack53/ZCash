from flask_server import app, blockchain
from flask import Flask, request

@app.route('/')
def rootRoute():
    return 'Hello, World!'
