from django.urls import path

from .import views

urlpatterns=[

    path('',views.info,name='info'),
    #path('infosend',views.infosend,name='infosend'),
    path('cancel',views.cancel,name='cancel'),
    

]