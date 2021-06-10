from . import views
from django.urls import path

urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('profile',views.profile,name='profile'),
    path('editprofile',views.editprofile,name='editprofile'),
    path('logout',views.logoutProfile,name='logoutProfile'),
    path('sendmail',views.sendmail,name='sendmail'),
    # path('ticketinbox',views.ticketinbox,name='ticketinbox'),

]