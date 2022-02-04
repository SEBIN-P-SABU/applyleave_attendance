from django.urls import re_path
from .import views


urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^Applyleave$', views.Applyleave, name='Applyleave'),
    re_path(r'^Attendance$', views.Attendance, name='Attendance'),
    re_path(r'^Trainees_Calendar$', views.Trainees_Calendar, name='Trainees_Calendar'),
    re_path(r'^Trainees_Attendancetable$', views.Trainees_Attendancetable, name='Trainees_Attendancetable'),
    re_path(r'^Requestedleave$', views.Requestedleave, name='Requestedleave'),
    re_path(r'^Trainers_Calendar$', views.Trainers_Calendar, name='Trainers_Calendar'),
    re_path(r'^Trainers_Attendancetable$', views.Trainers_Attendancetable, name='Trainers_Attendancetable'),
    re_path(r'^applyleavesub$', views.applyleavesub, name='applyleavesub'),
    re_path(r'^trainers_leave$', views.trainers_leave, name='trainers_leave'),
    re_path(r'^trainees_leave$', views.trainees_leave, name='trainees_leave'),
]