FROM python:3.9-slim-buster

WORKDIR /game

ENV PYTHONUNBUFFERED=1

COPY Merlin/ .
COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT [ "./run2.sh" ]