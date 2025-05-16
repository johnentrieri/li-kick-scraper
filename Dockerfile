FROM python:3

LABEL org.opencontainers.image.source=https://github.com/johnentrieri/li-kick-scraper

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./app.py" ]