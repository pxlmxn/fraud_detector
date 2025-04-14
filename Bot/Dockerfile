FROM python:3.13-bookworm
ENV PYTHONBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE 1
RUN apt-get update && apt-get install python3-pip -y && pip install --upgrade pip
WORKDIR /bot/
COPY requirements.txt /bot/
RUN pip install --no-cache-dir -r requirements.txt
