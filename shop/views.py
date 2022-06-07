from django.shortcuts import render
from django.views.generic import ListView
from .models import *
from django.db import connection


def dictfetchall(cursor):
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]


class CatalogOfCakesListView(ListView):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM shop_cake")
    r = dictfetchall(cursor)
    model = Cake
    queryset = r
    template_name = 'test.html'
    context_object_name = 'cakes'
