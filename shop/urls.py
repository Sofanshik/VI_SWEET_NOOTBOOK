from django.urls import path, include
from .views import *

urlpatterns = [
    path('', CatalogOfCakesListView.as_view()),
]