from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#new
def homePageView(request):
    return HttpResponse('Hello, World!')