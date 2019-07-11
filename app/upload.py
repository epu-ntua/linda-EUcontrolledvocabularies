# -*- coding: utf-8 -*-
"""
Created on Thu May 30 12:04:07 2019

@author: spele
"""

import os
import requests
from requests.exceptions import ConnectionError
import time
from elasticsearch import Elasticsearch
from pathlib import Path

#==============================================================================
# LICENCE
#==============================================================================
json_docs = []
for filename in os.listdir(os.getcwd()+ str(Path("/licence"))):
    if filename.endswith('.json'):
            json_docs.append(filename)
#==============================================================================
# define index name to work on
#==============================================================================
index_name =  "licence_index"
#==============================================================================
# Host name and authentication data
#==============================================================================
#local
host_name = "http://localhost:9200/"
auth = None

#server/cloud
#host_name = "https://d87782eb959c494189caf276b76755e0.eu-central-1.aws.cloud.es.io:9243/"
#auth = HTTPBasicAuth('elastic', 'Hu7JUDYL0zLzyLQsySuBnnEm')

#==============================================================================
#Wait till status yellow
#==============================================================================
url = host_name + index_name
es = Elasticsearch()
time.sleep(15)
es.cluster.health(wait_for_status= 'yellow', request_timeout= 100000000)
#==============================================================================
# DELETE OLD INDEX IF EXISTS
#==============================================================================
res = requests.delete(url, auth=auth)
print(res.status_code)
print(res.reason)

#==============================================================================
# Insert files
#==============================================================================

headers={"Content-Type" : "application/json"}

#os independent path
mapping = Path(os.getcwd()+"/licence/mapping/mapping.json")
#template = Path(os.getcwd()+"/mapping/template.json")
#res2 = requests.put(url+"_template/all", data=open(str(template), 'rb'), headers=headers,auth=auth)
#print(res2.status_code)
#print(res2.reason)

##create mapping
url = host_name + index_name
res = requests.put(url, data=open(str(mapping), 'rb'), headers=headers,auth=auth)
print(res.status_code)
print(res.reason)

##upload
headers={"Content-Type" : "application/json"}
i=0
res.status_code=200
while (((res.status_code == 200)or(res.status_code ==201)) and (i< len(json_docs))):
    print(i)
    url = host_name + index_name +"/_doc/" + str(i+1)
    res = requests.put(url, data=open(str(Path((os.getcwd()+"/licence/"+json_docs[i]))),'rb'), headers=headers,auth=auth)
    print(res.status_code)
    print(res.reason)
    i+=1


#==============================================================================
# COUNTRY
#==============================================================================
json_docs = []
for filename in os.listdir(os.getcwd()+ str(Path("/country"))):
    if filename.endswith('.json'):
            json_docs.append(filename)
#==============================================================================
# define index name to work on
#==============================================================================
index_name =  "country_index"
#==============================================================================
#Wait till status yellow
#==============================================================================
url = host_name + index_name
es = Elasticsearch()
es.cluster.health(wait_for_status= 'yellow', request_timeout= 100)
#==============================================================================
# DELETE previous index
#==============================================================================
res = requests.delete(url, auth=auth)
print(res.status_code)
print(res.reason)
#==============================================================================
# Insert files
#==============================================================================

headers={"Content-Type" : "application/json"}

#os independent path
mapping = Path(os.getcwd()+"/country/mapping/mapping.json")

##create mapping
url = host_name + index_name
res = requests.put(url, data=open(str(mapping), 'rb'), headers=headers,auth=auth)
print(res.status_code)
print(res.reason)

##upload
headers={"Content-Type" : "application/json"}
i=0
res.status_code=200
while (((res.status_code == 200)or(res.status_code ==201)) and (i< len(json_docs))):
    print(i)
    url = host_name + index_name +"/_doc/" + str(i+1)
    res = requests.put(url, data=open(str(Path((os.getcwd()+"/country/"+json_docs[i]))),'rb'), headers=headers,auth=auth)
    print(res.status_code)
    print(res.reason)
    i+=1

#==============================================================================
# LANGUAGE
#==============================================================================
json_docs = []
for filename in os.listdir(os.getcwd()+ str(Path("/language"))):
    if filename.endswith('.json'):
            json_docs.append(filename)
#==============================================================================
# define index name to work on
#==============================================================================
index_name =  "language_index"
#==============================================================================
#Wait till status yellow
#==============================================================================
url = host_name + index_name
es = Elasticsearch()
es.cluster.health(wait_for_status= 'yellow', request_timeout= 100)
#==============================================================================
# DELETE previous index
#==============================================================================
res = requests.delete(url, auth=auth)
print(res.status_code)
print(res.reason)
print(res.content)
#==============================================================================
# Insert files
#==============================================================================

headers={"Content-Type" : "application/json"}

#os independent path
mapping = Path(os.getcwd()+"/language/mapping/mapping.json")

##create mapping
url = host_name + index_name
res = requests.put(url, data=open(str(mapping), 'rb'), headers=headers,auth=auth)
print(res.status_code)
print(res.reason)

##upload
headers={"Content-Type" : "application/json"}
i=0
k=0
res.status_code=200
while (((res.status_code == 200)or(res.status_code ==201)) and (i< len(json_docs))):
    print(i)
    url = host_name + index_name +"/_doc/" + str(i+1)
    res = requests.put(url, data=open(str(Path((os.getcwd()+"/language/"+json_docs[i]))),'rb'), headers=headers,auth=auth)
    print(res.status_code)
    print(res.reason)
    while (res.status_code==403)and(k < 10):
            print(i)
            res = requests.put(url, data=open(str(Path((os.getcwd()+"/language/"+json_docs[i]))),'rb'), headers=headers,auth=auth)
            print(res.status_code)
            print(res.reason)
            k+=1
    i+=1
print(res.content)
