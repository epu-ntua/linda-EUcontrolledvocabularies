#!/bin/bash
docker-compose build
docker-compose up -d
docker exec -it es01 python get-pip.py && docker exec -it es01 pip install --trusted-host pypi.python.org -r requirements.txt && docker exec -it es01 python upload.py
docker exec -it es01 curl -XGET "localhost:9200/licence_index/_search?pretty" -H "Content-Type: application/json" -d @licence/query/query_url.json
docker exec -it es01 curl -XGET "localhost:9200/country_index/_search?pretty" -H "Content-Type: application/json" -d @country/query/query_url.json
docker exec -it es01 curl -XGET "localhost:9200/language_index/_search?pretty" -H "Content-Type: application/json" -d @language/query/query_url.json
