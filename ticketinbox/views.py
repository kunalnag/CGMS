from django.shortcuts import render
from .models import *
from .models import Product
from django.db.models import Q
from index.models import Customer
import datetime
from datetime import date,timedelta,time
from time import gmtime, strftime
import nltk
from textblob import TextBlob
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import redirect

# Create your views here.
def ticketinbox(request):
    if request.user.is_authenticated:
        priority=Priority.objects.all()
        source=Source.objects.all()
        status=Status.objects.all()
        executive=Executive.objects.all()
        ticket=Ticket.objects.all().select_related('assigned_to')
        ticket=ticket.order_by('-id')
        older=ticket.order_by('id')
        context={'ticket':ticket,
            'priority':priority,
            'source':source,
            'status':status,
            'executive':executive,'older':older}
        return render(request,'TicketInbox.html',context)
    else:
        return redirect('/')

def older(request):
    priority=Priority.objects.all()
    source=Source.objects.all()
    status=Status.objects.all()
    executive=Executive.objects.all()
    ticket=Ticket.objects.all().select_related('assigned_to')
    context={'ticket':ticket,
        'priority':priority,
        'source':source,
        'status':status,
        'executive':executive}

    return render(request,'TicketInbox.html',context)


def PriorityFilter(request,id):
    priority=Priority.objects.all()
    source=Source.objects.all()
    status=Status.objects.all()
    executive=Executive.objects.all()
    priorities=Priority.objects.get(priority=id)
    ticket=Ticket.objects.filter(ticket_priority=priorities)
    ticket=ticket.order_by('-id')
    context={
        'priority':priority,
        'source':source,
        'status':status,
        'executive':executive,
        'priorities':priorities,
        'ticket':ticket,
        
    }
    
    return render(request,'priority.html',context)

def StatusFilter(request,id):
    priority=Priority.objects.all()
    source=Source.objects.all()
    status=Status.objects.all()
    executive=Executive.objects.all()
    sta=Status.objects.get(status=id)
    ticket=Ticket.objects.filter(ticket_status=sta)
    ticket=ticket.order_by('-id')
    #print(priorities)
    context={
        'priority':priority,
        'source':source,
        'status':status,
        'executive':executive,
        'sta':sta,
        'ticket':ticket,
        
    }
    
    return render(request,'status.html',context)

def SourceFilter(request,id):
    priority=Priority.objects.all()
    source=Source.objects.all()
    status=Status.objects.all()
    executive=Executive.objects.all()
    src=Source.objects.get(source=id)
    ticket=Ticket.objects.filter(source=src)
    ticket=ticket.order_by('-id')

    context={
        'priority':priority,
        'source':source,
        'status':status,
        'executive':executive,
        'src':src,
        'ticket':ticket,
        
    }
    
    return render(request,'source.html',context)

def ExecutiveFilter(request,id):
    priority=Priority.objects.all()
    source=Source.objects.all()
    status=Status.objects.all()
    executive=Executive.objects.all()
    exe=Executive.objects.get(id=id)
    ticket=Ticket.objects.filter(assigned_to=exe)
    ticket=ticket.order_by('-id')

    context={
        'priority':priority,
        'source':source,
        'status':status,
        'executive':executive,
        'exe':exe,
        'ticket':ticket,
        
    }
    
    return render(request,'filter_exec.html',context)

def manual(request):
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
   
    return render(request,'manual.html')

def ticketdetail(request,id):
    #ticket=Ticket.objects.get(id=id)
    customer=Customer.objects.all()
    ticket=Ticket.objects.filter(id=id)
    executive=Executive.objects.all()
    tk=Ticket.objects.get(id=id)
    if tk.ticket_status != Status.objects.get(status="Closed"):
        tk.ticket_status=Status.objects.get(status="Open")
        print(tk.id)
        tk.save()
    x=tk.customer_id.customer_email
    print(x)
    email=Customer.objects.filter(customer_email= x)
    print(email)
    context={
        'ticket':ticket,
        'executive':executive,
        'email':email
    }
    if request.method=="POST":
        to=x
        info_title = request.POST["title"]
        info_content = request.POST['content']
        #customer_obj = Customer.objects.all()
        #customer_obj = Customer.objects.values('customer_email')
        #print(file_s)

        send_mail(
            info_title,
            info_content,
            settings.EMAIL_HOST_USER,
            [to],
            fail_silently=False,
        )
        tk.ticket_status=Status.objects.get(status="Open")
        #print(tk.id)
        tk.save()
        return render(request,'reply_send.html')
    

    return render(request,'ticket_details.html',context)

def closed(request,id):
    tkt=Ticket.objects.get(pk=id)
    tkt.ticket_status=Status.objects.get(status="Closed")
    tkt.save()

    if request.user.is_authenticated:
        priority=Priority.objects.all()
        source=Source.objects.all()
        status=Status.objects.all()
        executive=Executive.objects.all()
        ticket=Ticket.objects.all().select_related('assigned_to')
        ticket=ticket.order_by('-id')
        older=ticket.order_by('id')
        context={'ticket':ticket,
            'priority':priority,
            'source':source,
            'status':status,
            'executive':executive,'older':older}
        return render(request,'TicketInbox.html',context)
    else:
        return redirect('/')

def forword(request,id,id1):
    tkt=Ticket.objects.get(pk=id)
    #print(tkt)
    tkt.assigned_to=Executive.objects.get(id=id1)
    tkt.save()

    if request.user.is_authenticated:
        priority=Priority.objects.all()
        source=Source.objects.all()
        status=Status.objects.all()
        executive=Executive.objects.all()
        ticket=Ticket.objects.all().select_related('assigned_to')
        ticket=ticket.order_by('-id')
        older=ticket.order_by('id')
        context={'ticket':ticket,
            'priority':priority,
            'source':source,
            'status':status,
            'executive':executive,'older':older}
        return render(request,'TicketInbox.html',context)
    else:
        return redirect('/')




def ReplyTicket(request):
    return render(request,'reply_ticket_form.html')