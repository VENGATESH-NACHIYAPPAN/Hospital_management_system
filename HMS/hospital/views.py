
from django.shortcuts import render
from django.http import HttpResponse

from .models import Department, Doctor,Appointment
from .forms import PatientForm,ContactForm
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,'index.html')
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')

def department(request):
    dict_dept = {
        'dept_name': Department.objects.all()
    }
    return render(request, 'department.html',dict_dept)


def doctor(request):
    dict_doc={
        'doc': Doctor.objects.all()
    }
    return render(request,"doctor.html",dict_doc)


def patientregistration(request):
    if request.method == "POST":
        form= PatientForm(request.POST)
        if form.is_valid():
            form.save()
    form=PatientForm
    dict_form={
        'form': form
    }
    return render(request,"patient.html",dict_form)

def appointment(request):
    dict_appointment={
        'appointment': Appointment.objects.all()
    }
    return render(request,"appointment.html",dict_appointment)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Saves information directly to database
            messages.success(request, "Thank you for reaching out! Your inquiry has been submitted to the admin panel.")
            return redirect('contact')  # Redirects back cleanly to avoid multi-submit bugs
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})