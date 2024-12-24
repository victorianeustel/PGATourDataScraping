from data_queries.graphql import *
from classes.graphql.graphql_types import *

import csv

types_json = get_schema_types()
# print(types["data"]["__schema"]["types"])

types = [GraphQLType(**t).ToArray() for t in types_json["data"]["__schema"]["types"]]
with open("data/graphql/schema_types.csv", "w") as f:
    writer = csv.writer(f, delimiter=",")
    writer.writerow(GraphQLType.header)
    writer.writerows(types)

# for t in types:
#     print(t.name)