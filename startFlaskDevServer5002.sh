export FLASK_APP=flask_server
export FLASK_ENV=development
flask run -h localhost -p 5002 > output_flask_server5002.log 2>&1 &