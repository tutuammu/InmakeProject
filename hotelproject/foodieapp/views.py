
# from django.contrib import messages, auth

from django.shortcuts import render
from .models import blow
from .models import high

# Create your views here.
def home(request):
    obj=blow.objects.all()
    obj1=high.objects.all()
    return render(request,"index.html",{'result':obj,'result1':obj1})