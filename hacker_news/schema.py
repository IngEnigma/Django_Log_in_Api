import graphene
import graphql_jwt
import api_logs.schema
import links.schema
import users.schema

class Query(users.schema.Query, links.schema.Query, api_logs.schema.Query, graphene.ObjectType):
    pass

class Mutation(users.schema.Mutation, links.schema.Mutation, api_logs.schema.Mutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
