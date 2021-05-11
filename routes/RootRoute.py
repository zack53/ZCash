from flask_server import app

@app.route('/')
def rootRoute():
    return 'Hello, World!'
