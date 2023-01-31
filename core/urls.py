from django.urls import path
from .views import index, form_perrito, form_mod_vehiculo, form_del_vehiculo, form_contacto ,gatos, gusgus, estrella, pelusa, princesa, perros, chloe, lucas, philip, samantha, crud


urlpatterns = [
    path('',index,name="index"),
    path('contacto',form_contacto,name="form-contacto"),
    path('gatos',gatos,name='gatos'),
    path('gusgus',gusgus,name="Gusgus"),
    path('estrella',estrella,name='estrella'),
    path('pelusa',pelusa,name="pelusa"),
    path('princesa',princesa,name="princesa"),
    path('crud',crud,name="crud"),

    path('perros',perros,name='perros'),
    path('chloe',chloe,name='chloe'),
    path('lucas',lucas,name='lucas'),
    path('philip',philip,name='philip'),
    path('samantha',samantha,name='samantha'),





    path('form_perrito',form_perrito,name="form_perrito"),
    path('form-mod-vehiculo/<id>',form_mod_vehiculo,name="form_mod_vehiculo"),
    path('form-del-vehiculo/<id>',form_del_vehiculo,name="form_del_vehiculo"),
]