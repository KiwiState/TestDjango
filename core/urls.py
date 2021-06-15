from django.urls import path
from .views import home,artistas,bs,concepto,contacto,galeria,login,pint1,pint2,pint3,pint4,registro,subirobra

urlpatterns=[
    path('',home,name="home"),
    path('artistas/',artistas,name="artistas"),
    path('bs/',bs,name="bs"),
    path('concepto/',concepto,name="concepto"),
    path('contacto/',contacto,name="contacto"),
    path('galeria/',galeria,name="galeria"),
    path('login/',login,name="login"),
    path('pint1/',pint1,name="pint1"),
    path('pint2/',pint2,name="pint2"),
    path('pint3/',pint3,name="pint3"),
    path('pint4/',pint4,name="pint4"),
    path('registro/',registro,name="registro"),
    path('subirobra/',subirobra,name="subirobra"),




     
]
# create