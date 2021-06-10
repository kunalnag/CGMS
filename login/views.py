from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .form import CreateExecutiveForm
from django.contrib import messages
from index.views import dashboard
from login.models import Executive
from django.contrib.auth import authenticate,login,logout
from ticketinbox.models import Ticket
from django.contrib.auth.forms import AuthenticationForm






def register(request):
    form = CreateExecutiveForm()
    executive =  Executive() 
    if request.method == 'POST':
        form = CreateExecutiveForm(request.POST)
        # executive =  Executive()
        if form.is_valid():
            
            messages.success(request, 'Account Created Successfully !! : ')
            # name=request.POST.get('name')
            # fname = request.POST.get("first_name")
            # lname = request.POST.get("last_name")
            uname = request.POST.get("username")
            email = request.POST.get("email")

            # executive.executive_name=str(fname)+str(lname)
            # executive.executive_name=fname
            executive.executive_username=uname
            executive.executive_email=email

            form.save()
            print(uname,email)
            executive.save()
        else:
            form = CreateExecutiveForm()

           # user = form.cleaned_data.get('email')
           
       # return redirect('loginPage')
    context = {'form':form}
    return render(request,'loginmodule/index.html',context)


def loginPage(request):

       # if not request.user.is_authenticated:
    if request.method == 'POST':
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
                  
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname,  password=upass)

            # username = request.POST.get('email')
            # password = request.POST.get('password')

            if user is not None:
                login(request, user)
                messages.success(request,'Logged in Successfully!!')
                return redirect('dashboard')
            
    else:
                # messages.success(request, 'Username or Password is Incorrect')
        fm = AuthenticationForm()
    return render(request, 'loginmodule/index.html', {'form': fm})
    #########return render(request, 'login.html', {'form': fm})
                        
                   
                        
        # fm={}
        # return render(request, 'login.html', {'form': fm})
                    # return HttpResponseRedirect('/dashboard/')
        # else:
        #     fm = AuthenticationForm()
        #     messages.info(request, 'Username or Password is Incorrect')
        #     return render(request, 'login.html', {'form': fm})
    #else:
       # return HttpResponseRedirect('')


#logout


def user_logout(request):

    logout(request)
    # return redirect('loginPage')
    return render(request,'logout_form.html')   


# def forgot(request):
#         return render(request,'forgot.html')