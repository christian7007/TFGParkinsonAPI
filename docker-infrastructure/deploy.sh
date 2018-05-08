#!/bin/bash

if [ "$#" -ne 1 ]; then
	echo "Ilegal number of arguments"
	echo "sudo ./deploy.sh <api_port>"
else
	docker build -t tfgparkinson_api images/api/
	docker run --name="database" mongo &
	sleep 10
	docker run --link database --name="api" -p $1:5050 tfgparkinson_api &
fi
