from django.shortcuts import render
import datetime

# Create your views here.
def index(request):
    today = datetime.datetime.now()
    newyear = today.day == 1 and today.month == 1

    return render(request,"newyear/index.html",{
        "newyear": newyear
        })
    