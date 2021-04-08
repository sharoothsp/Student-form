from django.forms import ModelForm, TextInput
from django import forms

from .models import Sprofile


class SprofileForm(ModelForm):
    class Meta:
        model = Sprofile
        fields = ['First_name','Last_name','Reg_No','Phone_number']
        widgets = {'First_name':TextInput(attrs={'size':20}), 'Last_name':TextInput(attrs={'size':20}), 'Reg_No':TextInput(attrs={'size':20})}


class Searchform(forms.Form):
    search = forms.CharField(max_length=100)
