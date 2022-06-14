from .models import Cat
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CatSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
class AllCatsViewset(viewsets.ReadOnlyModelViewSet):

    queryset = Cat.objects.all()

    serializer_class = CatSerializer

@api_view(['GET'])
def filter_by_name(request):

    name = request.GET.get('q')

    breed = Cat.objects.get(breed__iexact=name)

    serializer = CatSerializer(breed, many=False)

    return Response(serializer.data, status=status.HTTP_200_OK)

def home(request):

    return render(request, 'index.html')