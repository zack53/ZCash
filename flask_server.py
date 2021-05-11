from flask import Flask, jsonify
from BlockchainModule.Blockchain import Blockchain
blockchain = Blockchain()
app = Flask(__name__, template_folder='templates', static_folder='templates', static_url_path='')

from routes import *
