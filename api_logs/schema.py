import graphene
from graphene_django.types import DjangoObjectType
from .models import APILog

class APILogType(DjangoObjectType):
    class Meta:
        model = APILog  
        fields = "__all__"

class Query(graphene.ObjectType):
    all_logs = graphene.List(
        APILogType,
        username=graphene.String(required=False),
        model=graphene.String(required=False),
    )

    def resolve_all_logs(self, info, username=None, model=None):
        queryset = APILog.objects.all()
        if username:
            queryset = queryset.filter(username=username)
        if model:
            queryset = queryset.filter(model=model)
        return queryset

class CreateAPILog(graphene.Mutation):
    class Arguments:
        username = graphene.String()
        model = graphene.String()  
        request_data = graphene.String()
        response_data = graphene.String()

    log = graphene.Field(APILogType)

    def mutate(self, info, username, model, request_data, response_data):
        log = APILog.objects.create(
            username=username,
            model=model,
            request_data=request_data,
            response_data=response_data,
        )
        return CreateAPILog(log=log)

class Mutation(graphene.ObjectType):
    create_log = CreateAPILog.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)