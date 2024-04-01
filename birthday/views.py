from django.shortcuts import render
import datetime
# Create your views here.

def index(request):
    day = datetime.datetime.now()
    
    birthday = day.day== 28 and day.month == 9
    
    return render(request, "birthday/index.html", {
        "birthday": birthday
    })
