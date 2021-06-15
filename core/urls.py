from django.urls import path
from .views import home,galeria,artistas,concepto,pint1

urlpatterns=[
    path('',home,name="home"),
    path('galeria/',galeria,name="galeria"),
    path('artistas/',galeria,name="artistas"),
    path('concepto/',galeria,name="concepto"),
    path('Pintura_uno/',galeria,name="pintura_1"),
     
]
# create