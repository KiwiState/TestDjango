from django.urls import path
from rest_pintura.views import lista_pintura,detalle_pintura

urlpatterns=[
    path('lista_pintura',lista_pintura,name="lista_pintura"),
    path('detalle_pintura/<id>',detalle_pintura,name="detalle_pintura"),
]
