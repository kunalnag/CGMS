from django.shortcuts import render
from django.http import HttpResponse
from login.models import Executive
from ticketinbox.models import Ticket
import datetime
import xlwt

def Reportsapp(request):
    return render(request,'Reports.html')

def agentperformance(request):
    obj1=Executive.objects.all().values('id','executive_name','assigned','total_responses','resolved','avg_response','avg_resolution')
    return render(request,'agent_performance.html',{'obj1': obj1})

def timesheetsummary(request):
    obj2=Executive.objects.all().values('id','executive_name','executive_email','avg_response','avg_resolution')
    return render(request,'show.html',{'obj2': obj2})

def ticketlifecycle(request):
    q1=Ticket.objects.filter(ticket_status='Closed').count()
    q2=Ticket.objects.filter(ticket_status='Unassigned').count()
    q3=Ticket.objects.filter(ticket_status='Unresolved').count()
    q4=Ticket.objects.filter(ticket_status='Overdue').count()
    return render(request,'Ticket_Life_Cycle.html',{'q1':q1,'q2':q2,'q3':q3,'q4':q4})

def customersurvey(request):
    obj4=Ticket.objects.all().values('id','assigned_to','created_on','ticket_rating')
    return render(request,'customer_survey.html',{'obj4':obj4})

def export_excel_agentperformance(request):
    response=HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition']='attachment; filename=Executive Performance ' +\
        str(datetime.datetime.now())+'.xls'
    wb=xlwt.Workbook(encoding='utf-8')
    ws=wb.add_sheet('Executive Performance ')
    row_num=0
    font_style=xlwt.XFStyle()
    font_style.font.bold=True
    columns=['id','executive_name','assigned','total_responses','resolved','avg_response','avg_resolution']
    for col_num in range(len(columns)):
        ws.write(row_num,col_num,columns[col_num],font_style)
    font_style=xlwt.XFStyle()
    rows=Executive.objects.all().values_list('id','executive_name','assigned','total_responses','resolved','avg_response','avg_resolution')
    for row in rows:
        row_num+=1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]),font_style)
    wb.save(response)
    return response

def export_excel_timesheetsummary(request):
    response=HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition']='attachment; filename=Timesheet Summary ' +\
        str(datetime.datetime.now())+'.xls'
    wb=xlwt.Workbook(encoding='utf-8')
    ws=wb.add_sheet('Timesheet Summary ')
    row_num=0
    font_style=xlwt.XFStyle()
    font_style.font.bold=True
    columns=['E_ID','E_Name','Email','Average_Response_Time','Average_Resolution_Time']
    for col_num in range(len(columns)):
        ws.write(row_num,col_num,columns[col_num],font_style)
    font_style=xlwt.XFStyle()
    rows=Executive.objects.all().values_list('id','executive_name','executive_email','avg_response','avg_resolution')
    for row in rows:
        row_num+=1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]),font_style)
    wb.save(response)
    return response

def export_excel_ticketlifecycle(request):
    response=HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition']='attachment; filename=Ticket lifecycle ' +\
        str(datetime.datetime.now())+'.xls'
    wb=xlwt.Workbook(encoding='utf-8')
    ws=wb.add_sheet('Ticket lifecycle ')
    row_num=0
    font_style=xlwt.XFStyle()
    font_style.font.bold=True
    columns=['Tickets_Status','Tickets_Count']
    for col_num in range(len(columns)):
        ws.write(row_num,col_num,columns[col_num],font_style)
    font_style=xlwt.XFStyle()
    rows=Ticket.objects.all().values_list('ticket_status').distinct()
    for row in rows:
        row_num+=1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]),font_style)
    wb.save(response)
    return response

def export_excel_customersurvey(request):
    response=HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition']='attachment; filename=Customer Survey ' +\
        str(datetime.datetime.now())+'.xls'
    wb=xlwt.Workbook(encoding='utf-8')
    ws=wb.add_sheet('Customer Survey ')
    row_num=0
    font_style=xlwt.XFStyle()
    font_style.font.bold=True
    columns=['Ticket Id','Executive ID','Date','Rating']
    for col_num in range(len(columns)):
        ws.write(row_num,col_num,columns[col_num],font_style)
    font_style=xlwt.XFStyle()
    rows=Ticket.objects.all().values_list('id','assigned_to','created_on','ticket_rating')
    for row in rows:
        row_num+=1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]),font_style)
    wb.save(response)
    return response
