from data_queries.pga.api import *
import requests

data = {
    "query": "query {\n __schema { \n types { \n name \n kind \n} \n} \n}"
}

response = requests.post(PGA_API.url, headers=PGA_API.headers, json=data)
x = response.json()
print(x)
