FROM python:3.8-slim-buster
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
#COPY . .
VOLUME /app
WORKDIR /app
# EXPOSE 80
EXPOSE ${CONSUMER_PORT}
ENTRYPOINT [ "python3" ]
CMD ["consumer.py" ]
