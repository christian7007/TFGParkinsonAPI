#use official Apache HTTP Server image as a parent
FROM ubuntu:16.04

#update the system
RUN apt-get update -y && apt-get upgrade -y

#instal needed software
RUN apt-get install -y git python-pip

#instal eve
RUN pip install eve

#clone REST API repository
RUN git clone https://github.com/christian7007/TFGParkinsonAPI.git

EXPOSE 5050

CMD ["python", "TFGParkinsonAPI/api/api.py"]
