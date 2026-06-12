from django.db import models

# Create your models here.

class Department(models.Model):
    department_name = models.CharField(max_length=100)
    department_description= models.TextField()

    def __str__(self):
        return self.department_name + ' ' + self.department_description


class Doctor(models.Model):
    doctor_name = models.CharField(max_length=100)
    doctor_specialization= models.TextField()
    doctor_image= models.ImageField(upload_to="doctor")
    department_name= models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.doctor_name

class Patient(models.Model):
    patient_name=models.CharField(max_length=50)
    patient_age= models.IntegerField()
    patient_phone= models.CharField()
    patient_email= models.EmailField()
    patient_problem= models.TextField()
    def __str__(self):
        return self.patient_name

class Appointment(models.Model):
    patient_name = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor_name = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_date= models.DateField()
    appointment_time= models.TimeField()


class Contact(models.Model):
    name = models.CharField(max_length=150, verbose_name="Patient Name")
    email = models.EmailField(verbose_name="Email Address")
    subject = models.CharField(max_length=250, verbose_name="Subject Matter")
    message = models.TextField(verbose_name="Detailed Message")
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Inquiries"

    def __str__(self):
        return f"{self.subject} - {self.name}"

