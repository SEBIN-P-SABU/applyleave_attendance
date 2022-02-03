from django.http import request
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')
def ApplyLeave(request):
    return render(request, 'ApplyLeave.html')
def Attendance(request):
    return render(request, 'Attendance.html')

