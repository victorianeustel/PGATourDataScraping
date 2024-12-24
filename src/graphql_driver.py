from data_queries.graphql import *
from classes.graphql.graphql_types import *

import csv
import pandas as pd

types_json = get_schema_types()

types = [GraphQLType(**t).ToArray() for t in types_json["data"]["__schema"]["types"]]
with open("data/graphql/schema_types.csv", "w") as f:
    writer = csv.writer(f, delimiter=",")
    writer.writerow(GraphQLType.header)
    writer.writerows(types)

# Schema Types
types_df = pd.read_csv("data/graphql/schema_types.csv")
# print(types_df["kind"].drop_duplicates())

# Object Fields
objects_df = types_df[types_df["kind"] == "OBJECT"]
object_names = objects_df["type_name"].tolist()

with open("data/graphql/schema_object_fields.csv", "w") as f:
    writer = csv.writer(f, delimiter=",")
    writer.writerow(GraphQLObjectField.header)
    
    for index, o in enumerate(object_names):
        print("OBJECT {0} ({1} / {2})"
            .format(o, 
                    index, 
                    len(object_names)
                    ), 
            end='\r'
            )
        object_fields_json = get_object_fields(o)
        object = GraphQLObject(**object_fields_json["data"]["__type"])
        object_fields = [f.ToArray() for f in object.fields]
        writer.writerows(object_fields)

# Enums
enums_df = types_df[types_df["kind"] == "ENUM"]
enum_names = enums_df["type_name"].tolist()
with open("data/graphql/schema_enum_values.csv", "w") as f:
    writer = csv.writer(f, delimiter=",")
    writer.writerow(GraphQLEnum.header)
    
    for index, e in enumerate(enum_names):
        print("ENUM {0} ({1} / {2})"
            .format(e, 
                    index, 
                    len(enum_names)
                    ), 
            end='\r'
            )
        enums_fields_json = get_enum_values(e)
        fields = enums_fields_json["data"]["__type"]
        enum_fields = GraphQLEnum(**fields).ToArray()
        writer.writerow(enum_fields)