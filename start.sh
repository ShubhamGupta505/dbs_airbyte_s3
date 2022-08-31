#!/bin/bash

echo =======================================
echo Hey Shubham, Welcome
echo =======================================

sleep 3

docker-compose up -d

# docker exec -it kafka /bin/bash

docker exec -it kafka pip install kafka-python
docker exec -it kafka wget https://bootstrap.pypa.io/pip/2.7/get-pip.py
docker exec -it kafka python get-pip.py
docker exec -it kafka pip install --upgrade setuptools
docker exec -it kafka pip install pandas
docker exec -it kafka pip install pyarrow
docker exec -it kafka pip install pandasql
docker exec -it kafka pip install boto3
docker exec -it kafka python /home/consumer.py
