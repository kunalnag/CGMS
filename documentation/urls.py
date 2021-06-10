from . import views
from django.urls import path

urlpatterns = [
    path('',views.documentation,name='documentation'),
]