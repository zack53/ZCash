export FLASK_APP=flask_server
export FLASK_ENV=development
flask run -h localhost -p 5001 > output_flask_server5001.log 2>&1 &