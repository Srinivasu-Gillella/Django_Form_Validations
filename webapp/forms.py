from django import forms
from django.core import validators

#Customized Forms
class EmpForm(forms.Form):
    Name=forms.CharField()
    Salary=forms.IntegerField()
    Opinion=forms.CharField(widget=forms.Textarea,validators=[validators.MaxLengthValidator(40),validators.MinLengthValidator(10)])