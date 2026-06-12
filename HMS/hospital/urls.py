from django.urls import path,include

from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('home/',views.home,name='home'),
    path('about',views.about,name='about'),
    path('department',views.department,name='department'),
    path('doctor',views.doctor,name='doctor'),
    path('patientregistration',views.patientregistration,name='patientregistration'),
    path('appointment/',views.appointment,name='appointment'),
    path('contact',views.contact, name='contact'),
]
