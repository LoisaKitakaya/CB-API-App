from . import views
from django.urls import path, include
from graphene_django.views import GraphQLView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('all_breeds', views.AllCatsViewset, basename='all_breeds')

urlpatterns = [
    # api endpoints
    path('rest/', include(router.urls)),
    path('graphql/', GraphQLView.as_view(graphiql=True)),
    path('rest/breed_name/', views.filter_by_name, name='breed_name'),

    # templates
    path('home/', views.home, name='home'),
]