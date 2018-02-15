FROM python:3.6

# Prepare app folder
RUN mkdir /app

# Install dependencies
COPY ./requirements.* /app/
RUN pip install -r /app/requirements.txt -r /app/requirements.dev.txt

COPY . /app
WORKDIR /app

RUN pip install -e .
CMD cuve.order --config /app/etc/config/development.yml server --host 0.0.0.0 --port 8080