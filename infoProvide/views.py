from django.shortcuts import render,redirect
from django.http import HttpResponse
from infoProvide.models import Provider
from django.core.mail import send_mail
from django.conf import settings
from index.views import dashboard
from index.models import Customer

def info(request):
    if request.method=="POST":
        info_category = request.POST["category"]
        info_title = request.POST["title"]
        info_description = request.POST['description']
        obj_provider = Provider(category=info_category,title=info_title,description=info_description)
        obj_provider.save()
        #customer_obj = Customer.objects.all()
        #customer_obj = Customer.objects.values('customer_email')
        
        file_s = Customer.objects.values_list('customer_email', flat=True).order_by('customer_email')
        #print(file_s)

        send_mail(
            info_title,
            info_description,
            settings.EMAIL_HOST_USER,
            file_s,
            fail_silently=False,
        )
        return render(request,'infosend.html')

    return render(request, 'alert.html')

# def infosend(request):
#     if request.method == "POST":
#         info_title = request.POST["title"] 
#         info_description = request.POST['description']
#         send_mail(
#             info_title,
#             info_description,
#             settings.EMAIL_HOST_USER,
#             ['kyogi3125@gmail.com','yogi.nit.mca@gmail.com'],
#             fail_silently=False,
#         )
#         return render(request,'infosend.html')
#     return render(request,'alert.html') 

def cancel(request):
    return redirect('dashboard')

