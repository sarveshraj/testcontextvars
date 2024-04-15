numOfRequests=${1:-10}

echo "Starting django server..."

python manage.py migrate &> /dev/null
python manage.py runserver &> logs.txt &

sleep 3

pong=$(curl --no-progress-meter http://localhost:8000/ping)
if [[ ${pong} != "pong" ]];then
    echo "Failed to start server. Exiting..."
    exit 1
fi

echo "Creating config file with ${numOfRequests} requests..."

> config.txt

for ((i=1;i<=$numOfRequests;i++)); 
do 
   echo "url = \"http://localhost:8000\"" >> config.txt
done

echo "Sending ${numOfRequests} requests in parallel..."

curl --no-progress-meter --parallel --parallel-immediate --config config.txt

echo "Killing server..."
kill $(lsof -t -i:8000) &> /dev/null

echo "Test complete. Check logs.txt."
