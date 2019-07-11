# Linda EU controlled vocabularies

Linda EU controlled vocabularies provides an elastic search api for the Eu controlled vocabularies (https://publications.europa.eu/en/web/eu-vocabularies/controlled-vocabularies)
Currently license, country and language are supported. 

1. Open Docker Quick start terminal / Linux terminal and set this folder as wd (cd /.../final_docker_all)

2. Open the file "settings.txt"and follow instructions depending on your system, so as to set higher memory limits required by elasticsearch.

3. Type bash ./script.sh and press Enter to run the elasticsearch application.
	The following actions will take place automatically:
		- Building of the container image based on the Dockerfile
		- Composition of container as demonstrated in docker-compose.yml and copy of local files inside the container as demonstrated inside the Dockerfile
		- Pip installation inside the container, installation of the libraries described inside requirements.txt & running of the upload.py python script to index the licences into elasticsearch container
		  (46 shards should be created inside the index "licence_index")
		- example valid queries, based on url, on every of the 3 indexes to check functionality of the installation.

4. Below you can see an example of how a query should be performed:
```
docker exec -it es01 curl <query> (e.g -> -XGET "localhost:9200/licence_index/_search?pretty" -H "Content-Type: application/json" -d @query/query_url.json)
```

Enjoy!
