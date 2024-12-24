from data_queries.pga.api import *
import requests

def get_schema_types():
    data = {
        "query": "query {\n __schema { \n types { \n name \n kind \n description \n} \n} \n}"
    }

    response = requests.post(PGA_API.url, headers=PGA_API.headers, json=data)
    return response.json()
    
def get_enum_values(enum_name: str = "CourseStatsId"):
    data = {
        "query": 
            "query { \n __type(name: " + 
            "\"{0}\"".format(enum_name) + ") { \n name \n enumValues{ \n name \n} \n} \n }"
    }

    response = requests.post(PGA_API.url, headers=PGA_API.headers, json=data)
    return response.json()

def get_object_fields(object_name: str = "Course"):
    data = {
        "query": 
            "query { \n __type(name: \"" + object_name + "\") { \n name \n fields { \n name \n type { \n name \n kind \n } \n } \n } \n} "
    }

    response = requests.post(PGA_API.url, headers=PGA_API.headers, json=data)
    return response.json()

    