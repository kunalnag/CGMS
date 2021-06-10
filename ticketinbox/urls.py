from . import views
from django.urls import path

urlpatterns = [
    path('',views.ticketinbox,name='ticketinbox'),
    path('older',views.older,name='older'),
    path('PriorityFilter/<str:id>/',views.PriorityFilter,name='PriorityFilter'),
    path('StatusFilter/<str:id>/',views.StatusFilter,name='StatusFilter'),
    path('SourceFilter/<str:id>/',views.SourceFilter,name='SourceFilter'),
    path('ExecutiveFilter/<str:id>/',views.ExecutiveFilter,name='ExecutiveFilter'),
    path('ticketdetail/<str:id>',views.ticketdetail,name='ticketdetail'),
    path('closed/<str:id>/',views.closed,name='closed'),
    path('manual',views.manual,name='manual'),
    path('forword/<str:id>-<str:id1>',views.forword,name='forword'),
    path('replay',views.ReplyTicket,name='ReplyTicket'),

]