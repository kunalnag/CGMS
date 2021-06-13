from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .form import CreateExecutiveForm
from django.contrib import messages
from index.views import dashboard
from login.models import Executive
from django.contrib.auth import authenticate,login,logout
from ticketinbox.models import Ticket
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


def register(request):
    form = User()
    executive=Executive()
    if request.method == 'POST':
        
        messages.success(request, 'Account Created Successfully !! : ')
        # name=request.POST.get('name')
        fname = request.POST.get("first_name")
        lname = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        print(username)
        name=fname+" "+lname
        #print(name)
        #executive.executive_name=str(fname)+str(lname)
        executive.executive_name=name
        executive.executive_username=username
        executive.executive_email=email
        form=User.objects.create_user(username=username, email=email, password=password)
        
        form.save()
        executive.id=110
        executive.save()

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
                        
                   
                        
        


#logout


def user_logout(request):

    logout(request)
    # return redirect('loginPage')
    return render(request,'logout_form.html')   


# def forgot(request):
#         return render(request,'forgot.html')