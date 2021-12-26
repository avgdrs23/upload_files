FROM python:3-slim

RUN pip install flask

RUN mkdir data

COPY upload_data.py  /

CMD ["/upload_data.py"]
