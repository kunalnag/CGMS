from django.urls import path

from .import views

urlpatterns=[
    path('',views.index,name='index'),
    path('support',views.support,name='support'),  
    path('form',views.feedback,name='feedback'),  
    path('status', views.check_status, name = 'check_status') ,
       
    path('thanku',views.thanku,name='thanku'), 
    path('track',views.complainTracking,name='complainTracking'),  
    
]