export FLASK_APP=flask_server
export FLASK_ENV=development
flask run -h localhost -p 5003 > output_flask_server5003.log 2>&1 &