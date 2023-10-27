FROM python:latest

WORKDIR /usr/src/scraper
COPY requirements.txt ./

RUN pip install -r requirements.txt
RUN pip install psycopg2-binary

#ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.11.0/wait /wait
#RUN chmod +x /wait

COPY . .
CMD ["sh", "-c", "sleep 10 && scrapy crawl scraper"]

