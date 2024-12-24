class GraphQLType():
    header = ["type_name", "kind", "description"]
    def __init__(self, name, kind, description):
        self.name = name
        self.kind = kind
        self.description = description
    
    def ToArray(self):
        return [self.name, self.kind, self.description]
        
class GraphQLEnum(): 
    header = ["enum_name", "enum_values"]
    def __init__(self, name, enumValues):
        self.enumName = name
        self.enumValues = [e["name"] for e in enumValues]
        
    def ToArray(self):
        return [self.enumName, self.enumValues]
        
# class GraphQLEnumValue():
#     def __init__(self, name, kind):
#         self.enumName = name
#         self.enumValues = enumValues


class GraphQLObject(): 
    # header = ["object_name", "fields"]
    def __init__(self, name, fields):
        self.name = name
        self.fields = [GraphQLObjectField(name, **o) for o in fields]
        
    # def ToArray(self):
    #     return [self.enumName, self.enumValues]
    
class GraphQLObjectField(): 
    header = ["object_name", "field_name", "field_type", "field_description"]
    def __init__(self, object_name, name, type):
        self.objectName = object_name
        self.name = name
        self.kind = type["kind"]
        self.description = type["description"]
        
    def ToArray(self):
        return [self.objectName, self.name, self.kind, self.description]