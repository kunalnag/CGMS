from django.urls import path
from . import views

urlpatterns=[

    path('',views.Reportsapp,name='Reportsapp'),
    path('executiveperformance',views.agentperformance,name='executiveperformance'),
    path('ticketlifecycle',views.ticketlifecycle,name='ticketlifecycle'),
    path('customersurvey',views.customersurvey,name='customersurvey'),
    path('timesheetsummary', views.timesheetsummary, name = "timesheetsummary"),
    path('export_excel_agentperformance', views.export_excel_agentperformance, name = "export_excel_agentperformance"),
    path('export_excel_timesheetsummary', views.export_excel_timesheetsummary, name = "export_excel_timesheetsummary"),
    path('export_excel_ticketlifecycle', views.export_excel_ticketlifecycle, name = "export_excel_ticketlifecycle"),
    path('export_excel_customersurvey', views.export_excel_customersurvey, name = "export_excel_customersurvey"),
]