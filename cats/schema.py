import graphene
from .models import Cat
from graphene_django import DjangoObjectType

class BreedType(DjangoObjectType):

    class Meta:

        model = Cat

        fields = '__all__'

class Query(graphene.ObjectType):

    all_breeds = graphene.List(BreedType)

    breed_by_name = graphene.Field(BreedType, breed=graphene.String(required=True))

    def resolve_all_breeds(root, info):

        return Cat.objects.all()

    def resolve_breed_by_name(root, info, breed):

        return Cat.objects.filter(breed=breed).first()