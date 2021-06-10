
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('login.urls')),
    path('dashboard',include('index.urls')),       
    path('ticketinbox',include('ticketinbox.urls')),       
    path('report',include('Reportsapp.urls')),
    path('Charts',include('AllCharts.urls')),
    path('documentation',include('documentation.urls')),
    path('dashboard/help',include('support.urls')), 
    path('dashboard/feedback',include('support.urls')), 
    path('dashboard/complainTracking',include('support.urls')), 
    path('dashboard/complainTracking/checkStatus/',include('support.urls')), #for status track
    path('dashboard/support',include('complainTracking.urls')), 
    path('dashboard/complainTracking', include('complainTracking.urls')),
    path('dashboard/info', include('infoProvide.urls')),


    # path('',ClubChartView.as_view(), name='home')      
]
