from django.http import request
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def Applyleave(request):
    return render(request, 'Applyleave.html')
    
def Attendance(request):
    return render(request, 'Attendance.html')

def Trainees_Calendar(request):
    return render(request, 'Trainees_Calendar.html')
def Trainees_Attendancetable(request):
    return render(request, 'Trainees_Attendancetable.html')

def Requestedleave(request):
    return render(request, 'Requestedleave.html')

def Trainers_Attendancetable(request):
    return render(request, 'Trainers_Attendancetable.html')
def Trainers_Calendar(request):
    return render(request, 'Trainers_Calendar.html')

def applyleavesub(request):
    return render(request, 'applyleavesub.html')

def trainers_leave(request):
    return render(request, 'trainers_leave.html')
def trainees_leave(request):
    return render(request, 'trainees_leave.html')

