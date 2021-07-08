from django.urls import path
from .views import home,artistas,bs,concepto,contacto,galeria,login,pint1,pint2,pint3,pint4,registro,subirobra,form_list_mod_pintura,form_mod_pintura,form_del_pintura,pintura_fill

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
    path('form-mod_list-pintura/',form_list_mod_pintura,name="form_mod_list_pintura"),
    path('form-mod-pintura/<id>',form_mod_pintura,name="form_mod_pintura"),
    path('form-del-pintura/<id>',form_del_pintura,name="form_del_pintura"),
    path('pintura/<id>',pintura_fill,name="pintura"), ##auto change
]

# create