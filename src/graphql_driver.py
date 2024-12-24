from data_queries.graphql import *
from classes.graphql.graphql_types import *

import csv
import pandas as pd

# types_json = get_schema_types()

# types = [GraphQLType(**t).ToArray() for t in types_json["data"]["__schema"]["types"]]
# with open("data/graphql/schema_types.csv", "w") as f:
#     writer = csv.writer(f, delimiter=",")
#     writer.writerow(GraphQLType.header)
#     writer.writerows(types)

types_df = pd.read_csv("data/graphql/schema_types.csv")
enums_df = types_df[types_df["kind"] == "ENUM"]
enum_names = enums_df["type_name"].tolist()
# print(enum_names)


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