from django import forms
from django.contrib.auth.models import User
from django.forms import EmailInput, TextInput

from .models import Festival, Manager, Users


class DateInput(forms.DateInput):
    input_type = 'date'


class ManagerForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = Manager
        fields = ('email', 'password')


class FestivalForm(forms.ModelForm):

    class Meta:
        model = Festival
        fields = ['name', 'start_date', 'finish_date', 'country', 'city', 'address', 'image', 'description']
       
       
        widgets = {
            'start_date': DateInput(attrs={'class': "form-control", 'style': 'max-width: 300px;',}),
            'finish_date': DateInput(attrs={'style': 'width: 300px'}),
            'name': TextInput(attrs={'class': "form-control", 'style': 'max-width: 300px;'}),
            'description': forms.Textarea(attrs={'class': 'textarea', 'style': 'width: 50%;', 'placeholder' : 'Describe festival...'}),
        }
        
class UserForm(forms.ModelForm):

    class Meta:
        model = Users
        fields = ['first_name', 'last_name', 'email', 'festival']
        
       
       
        widgets = {
            'first_name': TextInput(attrs={'class': "form-control", 'style': 'max-width: 300px;'}),
            'last_name': TextInput(attrs={'class': "form-control", 'style': 'max-width: 300px;'}),
            'email': EmailInput(attrs={'class': "form-control", 'style': 'max-width: 300px;'}),
            'festival': forms.HiddenInput(),
        }

