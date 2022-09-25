FROM python:latest
RUN apt-get update
RUN apt-get install wget
RUN wget https://raw.githubusercontent.com/mschermann/forensic_accounting/master/fb_sub.csv
RUN pip install regex

ADD codelab1.py .
RUN python3 codelab1.py

#CMD ["python", "./codelab1.py"]
