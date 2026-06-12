# In your forms.py
from django import forms
from .models import Patient, Contact# or your specific model

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        widgets = {
            # This directly controls the height of the problem textbox
            'problem': forms.Textarea(attrs={'rows': 3}), 
        }




class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']