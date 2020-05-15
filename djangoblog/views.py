from django.shortcuts import render
from django.shortcuts import HttpResponse

def about(request):
    # return HttpResponse('hi there! hello world')
    return render(request,'about.html')

def home(request):
    # return HttpResponse("hello")
    return render(request,'home.html')
