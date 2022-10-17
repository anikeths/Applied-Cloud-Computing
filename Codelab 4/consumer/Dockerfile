FROM python:3.8-slim-buster
#WORKDIR /python-docker
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
#COPY . .
VOLUME /app
WORKDIR /app
EXPOSE 80
ENTRYPOINT [ "python3" ]
CMD ["consumer.py" ]
