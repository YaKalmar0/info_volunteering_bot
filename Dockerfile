FROM python:3.9-slim

USER root
WORKDIR /app

COPY requirements.txt /
RUN pip3 install -r /requirements.txt

COPY *.py /app/
COPY handlers/ /app/handlers/
COPY libs/ /app/libs/

CMD ["python3", "bot.py"]
