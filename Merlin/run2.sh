#!/bin/bash

# For docker
python runServer.py --replaysavepath /deerhunt/log.json --saveoutcome /deerhunt/result.json 8000 & 
sleep 0.5
python runClient.py 172.17.0.2 8000 & 
python runClient2.py 172.17.0.2 8000 &

# uncomment below to run on dev machine.
# python3 runServer.py 8000 & 
# sleep 0.5
# python3 runClient.py 127.0.1.1 8000 & 
# python3 runClient2.py 127.0.1.1 8000 &

# sleep 
wait