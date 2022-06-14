import graphene
from cats import schema

class Query(schema.Query, graphene.ObjectType):

    pass

schema = graphene.Schema(query=Query)