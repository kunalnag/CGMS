from django.shortcuts import render
from ticketinbox.models import Ticket
from login.models import Executive
from django.db.models import Q
from datetime import datetime,timedelta,time
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.db.models import Aggregate,Avg


# Create your views here.
def dashboard(request):
    if request.user.is_authenticated:
        
        Unresolved = Ticket.objects.filter(Q(ticket_status='Open')).count()
        Overdue = Ticket.objects.filter(Q(ticket_status='Overdue')).count()
        Closed = Ticket.objects.filter(Q(ticket_status='Closed')).count()
        Unassigned = Ticket.objects.filter(Q(ticket_status='Onhold')).count()

        #Queries related to Ticket Start by date
        today = datetime.today().date()
        dayback1 = today-timedelta(days=1)
        dayback3 = today-timedelta(days=3)
        dayback2 = today-timedelta(days=2)
        dayback4 = today-timedelta(days=4)
        dayback5 = today-timedelta(days=5)
        dayback6 = today-timedelta(days=6)
        
        tdayback1 = Ticket.objects.filter(created_on__date=today).count()
        tdayback2 = Ticket.objects.filter(created_on__date=dayback1).count()
        tdayback3 = Ticket.objects.filter(created_on__date=dayback2).count()
        tdayback4 = Ticket.objects.filter(created_on__date=dayback3).count()
        tdayback5 = Ticket.objects.filter(created_on__date=dayback4).count()
        tdayback6 = Ticket.objects.filter(created_on__date=dayback5).count()
        tdayback7 = Ticket.objects.filter(created_on__date=dayback6).count()
       
        week_days=["Mon","Tue","Wed","Thur","Fri","Sat","Sun"]
        
        weekno1 =  today.weekday()
        weekno2 =  dayback1.weekday()
        weekno3 =  dayback2.weekday()
        weekno4 =  dayback3.weekday()
        weekno5 =  dayback4.weekday()
        weekno6 =  dayback5.weekday()
        weekno7 =  dayback6.weekday()
      
        d1 = week_days[weekno1]
        d2 = week_days[weekno2]
        d3 = week_days[weekno3]
        d4 = week_days[weekno4]
        d5 = week_days[weekno5]
        d6 = week_days[weekno6]
        d7 = week_days[weekno7]

        unhappy = Ticket.objects.filter(ticket_rating__lte=1).count()
        ok = Ticket.objects.filter(ticket_rating__range=(2,3)).count()
        happy = Ticket.objects.filter(ticket_rating__range=(4,5)).count()
        
        no_of_webform = Ticket.objects.filter(Q(source='Web-form')).count()
        no_of_email = Ticket.objects.filter(Q(source='Email')).count()
        no_of_socialmedia = Ticket.objects.filter(Q(source='Social-media')).count()

        avg_responce_time = Executive.objects.all().aggregate(Avg('avg_response'))
        avg_resolve_time = Executive.objects.all().aggregate(Avg('avg_resolution'))

        avg_resp = avg_responce_time.get("avg_response__avg")
        avg_resolve = avg_resolve_time.get("avg_resolution__avg")

        today = datetime.now()

        dashboard_data = {
            "unresolved":Unresolved,
            "overdue":Overdue,
            "closed": Closed,
            "unassigned":Unassigned ,
            "no_of_webform":no_of_webform,
            "no_of_email":no_of_email,
            "no_of_socialmedia":no_of_socialmedia,
            "avg_resolve_time":avg_resolve,
            "avg_responce_time":avg_resp,
            
            "happy":happy,
            "ok":ok,
            "unhappy":unhappy,

            "today":today,
            "name":request.user,

            "day1":d1,
            "day2":d2,
            "day3":d3,
            "day4":d4,
            "day5":d5,
            "day6":d6,
            "day7":d7,

            "tcount1":tdayback1,
            "tcount2":tdayback2,
            "tcount3":tdayback3,
            "tcount4":tdayback4,
            "tcount5":tdayback5,
            "tcount6":tdayback6,
            "tcount7":tdayback7,
            
        }
        return render(request,'dashboard.html', dashboard_data)
    else:
        return redirect('/')


      


# executive_profile view
def profile(request):
    if request.user.is_authenticated:
        executive_data = Executive.objects.filter(executive_email=request.user.email)
        return render(request,'executive_profile.html',{'executive_data':executive_data})
    else:
        return redirect('/')


def editprofile(request):
    return render(request,'edit_profile_form.html')

def logoutProfile(request):
    logout(request)
    return render(request,'logout_form.html')

def ticketinbox(request):
    return render(request,'TicketInbox.html',)


# function for sending mail
def sendmail(request):
    import easyimap as e
    host = "imap.gmail.com"
    user = "contactus.probotiq@gmail.com"
    password = "probotiqteam4"
    from django.core.mail import EmailMessage
    from django.conf import settings
    from django.template.loader import render_to_string
   
    server = e.connect(host, user, password)
    for i in server.listids(limit=3): #listids use for updated emails
        emaill=server.mail(i)
        eid = emaill.from_addr
        print(eid)
        p = eid.split('<')[1]
        print(p)
        emailid = p.split('>')[0]
        print(emailid)


        #emailid is the full email
        template = render_to_string('email_template.html')
        email = EmailMessage(
            'Probotiq Solutions Support',
            template,
            settings.EMAIL_HOST_USER,
            [emailid],
        )
        email.fail_silently=False,
        email.send()

    server.quit()
        
    return render(request,'sendmail.html')