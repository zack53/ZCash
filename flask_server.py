from flask import Flask, jsonify
from BlockchainModule.ZCash import ZCash
from uuid import uuid4
nodeAddress = str(uuid4()).replace('-','')
blockchain = ZCash()
app = Flask(__name__, template_folder='templates', static_folder='templates', static_url_path='')

from routes import *
