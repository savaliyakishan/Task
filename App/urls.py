from django.urls import path
from . import views
from graphene_django.views import GraphQLView
from App.schema import schema



urlpatterns = [
    path("",views.index,name="Home"),
   
]
