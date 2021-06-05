from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def MyWelcome(request):
    return render(request,'test.html')    