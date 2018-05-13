#!/bin/bash

if [ "$#" -ne 2 ]; then
	echo "Ilegal number of arguments"
	echo "sudo ./deploy.sh <api_port> <web_port>"
else
	docker build -t tfgparkinson_api images/api/	

	git clone https://github.com/al3xhh/TFGParkinsonWeb.git ./images/webserver/TFGParkinsonWeb	

	docker build -t tfgparkinson_server images/webserver

	docker run -d --name="database" mongo
	sleep 10
	docker run -d --link database --name="api" -p $1:5050 tfgparkinson_api
	sleep 10 
	docker run -d --link api --name="web_server" -p $2:80 tfgparkinson_server
	sleep 10
	rm -rf ./images/webserver/TFGParkinsonWeb
fi
