from django.forms import ModelForm
from django import forms
from .models import Employee
class EmployeeForm(ModelForm):
    class Meta:
        model=Employee
        fields='__all__'
        widgets={
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'address': forms.TextInput(attrs={'class':'form-control'}),
            'skill': forms.TextInput(attrs={'class':'form-control'}),
        }