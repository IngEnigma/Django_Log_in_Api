import graphene
from graphene_django.types import DjangoObjectType
from .models import APILog

class APILogType(DjangoObjectType):
    class Meta:
        model = APILog  

class Query(graphene.ObjectType):
    all_logs = graphene.List(APILogType)

    def resolve_all_logs(self, info):
        return APILog.objects.all()

class CreateAPILog(graphene.Mutation):
    class Arguments:
        user = graphene.String()
        request_data = graphene.String()
        response_data = graphene.String()

    log = graphene.Field(APILogType)

    def mutate(self, info, user, request_data, response_data):
        log = APILog.objects.create(user=user, request_data=request_data, response_data=response_data)
        return CreateAPILog(log=log)

class Mutation(graphene.ObjectType):
    create_log = CreateAPILog.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)