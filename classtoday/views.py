from django.shortcuts import render
import datetime

def index(request):
    now = datetime.datetime.now()
    classtoday = now.weekday()== 0 or now.weekday()==2
    return render(request, "classtoday/index.html", 
        {"currenttime": now,
         "classtoday": classtoday})
