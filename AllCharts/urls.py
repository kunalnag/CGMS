from django.urls import path

from .import views

urlpatterns=[
    path('',views.Charts,name='Charts'),
    path('chart',views.chart,name='chart'),
    path('Average_Ticket_Response',views.Average_Ticket_Response,name='Average_Ticket_Response'),
    path('Average_Ticket_Resolution',views.Average_Ticket_Resolution,name='Average_Ticket_Resolution'),
    path('TicketStatistics', views.TicketStatistics, name='TicketStatistics'),
    path('rating', views.customerRating, name='customerRating'),
    path('auto',views.auto,name='auto'),
]