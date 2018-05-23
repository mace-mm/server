import graphene

import topic.schema


class Query(topic.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)

