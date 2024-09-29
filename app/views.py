from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def App_Creation(request):
    return HttpResponse('App Creation in the Django-Project')

def first(request):
    return render(request,"first.html")


