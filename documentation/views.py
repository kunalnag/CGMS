from django.shortcuts import render

# Create your views here.
def documentation(request):
    return render(request,'documentation.html')