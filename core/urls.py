from django.urls import path
from .views import home,galeria,pint1

urlpatterns=[
    path('',home,name="home"),
    path('galeria/',galeria,name="galeria"),
    path('Pintura_uno/',galeria,name="pintura_1"),
     
]
# create