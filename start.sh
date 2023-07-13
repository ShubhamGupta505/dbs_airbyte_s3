#!/bin/bash

echo =======================================
echo Hey Shubham, Welcome
echo =======================================

sleep 3

docker-compose up -d

# docker exec -it kafka /bin/bash

docker exec -it kafka1 pip3 install kafka-python
docker exec -it kafka1 pip3 install pandas
docker exec -it kafka1 pip3 install pyarrow
docker exec -it kafka1 pip3 install pandasql
docker exec -it kafka1 pip3 install boto3
docker exec -it kafka1 touch /home/appuser/files/data.csv
docker exec -it kafka1 python /home/consumer.py
