export FLASK_APP=flask_server
export FLASK_ENV=development
flask run > output_flask_server.log 2>&1 &
echo 'Server has started successfully'
echo 'PID is located below:'
echo $(ps -a | grep 'flask')
