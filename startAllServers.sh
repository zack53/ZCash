./startFlaskDevServer5001.sh
./startFlaskDevServer5002.sh
./startFlaskDevServer5003.sh
echo 'Servers have started successfully'
echo 'PID is located below:'
echo $(ps -a | grep 'flask')
