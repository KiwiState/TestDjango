from django.urls import path
from rest_pintura.views import lista_pintura,detalle_pintura
from rest_pintura.viewslogin import login
urlpatterns=[
    path('lista_pintura',lista_pintura,name="lista_pintura"),
    path('detalle_pintura/<id>',detalle_pintura,name="detalle_pintura"),
    path('login',login,name ="login")
]
