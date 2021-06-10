from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def complainTracking(request):
    return render(request, 'complaint_tracking.html');