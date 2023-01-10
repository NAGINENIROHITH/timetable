from django.shortcuts import render

# Create your views here.

def timetable(request):
    return render(request,'webtimetable/timetable.html')