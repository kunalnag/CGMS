from django.shortcuts import render
from index.models import Customer
from .models import Feedback
from ticketinbox.models import *
from login.models import Executive
from django.http import HttpResponse
import datetime
from datetime import date,timedelta,time
from time import gmtime, strftime
import nltk
from textblob import TextBlob
# Create your views here.

def index(request):
    return render(request,'faq.html')

def thanku(request):
    return render(request,'thankyou_form.html')

def complainTracking(request):
    if request.method=='GET':
        search=request.GET.get('search')
        ticket=Ticket.objects.all().filter(id=search)
        print(ticket)
    return render(request, 'complaint_tracking.html',{'ticket':ticket})

def check_status(request):
    return render(request,'enter_complaint_id.html',)

def feedback(request):
    
    if request.method=="POST":
        fb=Feedback()
        
        rt = request.POST.get('experience') 
        ct = request.POST.get('comments')
        nm = request.POST.get('name')
        em = request.POST.get('email')
        
        fb.rating = rt 
        fb.text = ct
        fb.name = nm
        fb.email = em

        fb.save()
        return render(request,'feedbackdone.html')
    else:
        return render(request,'formpage.html',)




    

def support(request):
    if request.method=="POST":
        contact=Customer()
        tkt=Ticket()
        
        name=request.POST.get('name')
        orderid=request.POST.get('orderid')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        quetionstype=request.POST.get('quetionstype')
        subject=request.POST.get('subject')
        description=request.POST.get('description')
        Recommendation=request.POST.get('Recommendation')
        #rate=request.POST.get('rate')
        #images=request.POST.get('images')
        
        contact.customer_name=name
        contact.orderid=orderid
        contact.customer_email=email
        contact.customer_contact=phone
        contact.quetionstype=quetionstype

        contact.subject=subject
        contact.description=description
        contact.Recommendation=Recommendation
        #contact.rate=rate
       # contact.images=images

       #save data in Ticket table
        tkt.title=subject
        tkt.ticket_type=quetionstype

        blob_text=description
        blob = TextBlob(blob_text)
        polarity=blob.sentiment[0]
        if polarity < 0:
            tkt.ticket_priority=Priority.objects.get(priority="High")
        elif polarity > 0:
            tkt.ticket_priority=Priority.objects.get(priority="Low")
        else:
            tkt.ticket_priority=Priority.objects.get(priority="Medium")

        
        #assign tickets to executives
        lis=Executive.objects.all().values_list('id', flat=True)
        tkt.c=Ticket.objects.values_list('assigned_to',flat=True).last()
        tkt.x=tkt.c
        t=lis.last()
        if(tkt.x==None):
            tkt.x=lis[0]
            tkt.assigned_to_id=tkt.x
        elif(tkt.x==t):
            tkt.x=lis[0]
            tkt.x=tkt.x+1
            tkt.assigned_to_id=tkt.x
        else:
            tkt.x=tkt.x+1
            tkt.assigned_to_id=tkt.x

        tkt.assigned_dep=Executive.objects.filter(id=tkt.x).values('executive_dep')
        tkt.source=Source.objects.get(source="Web-form")
        tkt.ticket_status=Status.objects.get(status="Onhold")
        
        print(Customer.objects.all().last())
        Created_Date_and_Time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        tkt.created_on=Created_Date_and_Time

        #tkt.ticket_rating=int(rate)
        tkt.due_date=datetime.datetime.now()+datetime.timedelta(days=3)
        contact.save()
        tkt.customer_id=Customer.objects.all().last()
        tkt.save()
        


        

        last=Ticket.objects.all().last()
        return render(request,'thankyou_form.html',{'last':last})
   
    return render(request,'contact.html')

def supportEmail(request):
    if request.method=="POST":
        contact=Customer()
        tkt=Ticket()
        
        name=request.POST.get('name')
        orderid=request.POST.get('orderid')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        quetionstype=request.POST.get('quetionstype')
        subject=request.POST.get('subject')
        description=request.POST.get('description')
        Recommendation=request.POST.get('Recommendation')
        #rate=request.POST.get('rate')
        #images=request.POST.get('images')
        
        contact.customer_name=name
        contact.orderid=orderid
        contact.customer_email=email
        contact.customer_contact=phone
        contact.quetionstype=quetionstype

        contact.subject=subject
        contact.description=description
        contact.Recommendation=Recommendation
        #contact.rate=rate
       # contact.images=images

       #save data in Ticket table
        tkt.title=subject
        tkt.ticket_type=quetionstype

        blob_text=description
        blob = TextBlob(blob_text)
        polarity=blob.sentiment[0]
        if polarity < 0:
            tkt.ticket_priority=Priority.objects.get(priority="High")
        elif polarity > 0:
            tkt.ticket_priority=Priority.objects.get(priority="Low")
        else:
            tkt.ticket_priority=Priority.objects.get(priority="Medium")

        
        #assign tickets to executives
        lis=Executive.objects.all().values_list('id', flat=True)
        tkt.c=Ticket.objects.values_list('assigned_to',flat=True).last()
        tkt.x=tkt.c
        t=lis.last()
        if(tkt.x==None):
            tkt.x=lis[0]
            tkt.assigned_to_id=tkt.x
        elif(tkt.x==t):
            tkt.x=lis[0]
            tkt.x=tkt.x+1
            tkt.assigned_to_id=tkt.x
        else:
            tkt.x=tkt.x+1
            tkt.assigned_to_id=tkt.x

        tkt.assigned_dep=Executive.objects.filter(id=tkt.x).values('executive_dep')
        tkt.source=Source.objects.get(source="Email")
        tkt.ticket_status=Status.objects.get(status="Onhold")
        
        print(Customer.objects.all().last())
        Created_Date_and_Time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        tkt.created_on=Created_Date_and_Time

        #tkt.ticket_rating=int(rate)
        tkt.due_date=datetime.datetime.now()+datetime.timedelta(days=3)
        contact.save()
        tkt.customer_id=Customer.objects.all().last()
        tkt.save()
        


        

        last=Ticket.objects.all().last()
        return render(request,'thankyou_form.html',{'last':last})
   
    return render(request,'contact.html')


def supportSocial(request):
    if request.method=="POST":
        contact=Customer()
        tkt=Ticket()
        
        name=request.POST.get('name')
        orderid=request.POST.get('orderid')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        quetionstype=request.POST.get('quetionstype')
        subject=request.POST.get('subject')
        description=request.POST.get('description')
        Recommendation=request.POST.get('Recommendation')
        #rate=request.POST.get('rate')
        #images=request.POST.get('images')
        
        contact.customer_name=name
        contact.orderid=orderid
        contact.customer_email=email
        contact.customer_contact=phone
        contact.quetionstype=quetionstype

        contact.subject=subject
        contact.description=description
        contact.Recommendation=Recommendation
        #contact.rate=rate
       # contact.images=images

       #save data in Ticket table
        tkt.title=subject
        tkt.ticket_type=quetionstype

        blob_text=description
        blob = TextBlob(blob_text)
        polarity=blob.sentiment[0]
        if polarity < 0:
            tkt.ticket_priority=Priority.objects.get(priority="High")
        elif polarity > 0:
            tkt.ticket_priority=Priority.objects.get(priority="Low")
        else:
            tkt.ticket_priority=Priority.objects.get(priority="Medium")

        
        #assign tickets to executives
        lis=Executive.objects.all().values_list('id', flat=True)
        tkt.c=Ticket.objects.values_list('assigned_to',flat=True).last()
        tkt.x=tkt.c
        t=lis.last()
        if(tkt.x==None):
            tkt.x=lis[0]
            tkt.assigned_to_id=tkt.x
        elif(tkt.x==t):
            tkt.x=lis[0]
            tkt.x=tkt.x+1
            tkt.assigned_to_id=tkt.x
        else:
            tkt.x=tkt.x+1
            tkt.assigned_to_id=tkt.x

        tkt.assigned_dep=Executive.objects.filter(id=tkt.x).values('executive_dep')
        tkt.source=Source.objects.get(source="Social-media")
        tkt.ticket_status=Status.objects.get(status="Onhold")
        
        print(Customer.objects.all().last())
        Created_Date_and_Time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        tkt.created_on=Created_Date_and_Time

        #tkt.ticket_rating=int(rate)
        tkt.due_date=datetime.datetime.now()+datetime.timedelta(days=3)
        contact.save()
        tkt.customer_id=Customer.objects.all().last()
        tkt.save()
        


        

        last=Ticket.objects.all().last()
        return render(request,'thankyou_form.html',{'last':last})
   
    return render(request,'contact.html')