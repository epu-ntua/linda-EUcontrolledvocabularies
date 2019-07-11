FROM docker.elastic.co/elasticsearch/elasticsearch:7.1.1

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./app /app
