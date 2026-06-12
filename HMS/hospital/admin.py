from django.contrib import admin

from .models import Department, Doctor, Patient, Appointment,Contact

# Register your models here.
admin.site.register(Department)
admin.site.register(Doctor)
class PatientAdmin(admin.ModelAdmin):
     list_display=('patient_name','patient_age','patient_phone','patient_email','patient_problem')
admin.site.register(Patient,PatientAdmin)

admin.site.register(Appointment)



class ContactAdmin(admin.ModelAdmin):
    list_display = ('subject', 'name', 'email', 'submitted_at')
    list_filter = ('submitted_at',)
    search_fields = ('name', 'email', 'subject')
admin.site.register(Contact,ContactAdmin)
