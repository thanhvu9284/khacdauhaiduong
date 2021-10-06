from django import forms
from django.forms import widgets

class contact_Form(forms.Form):
    ten = forms.CharField(max_length=150)
    dienthoai = forms.CharField(max_length=50)
    email = forms.EmailField(widget = forms.EmailInput)
    noidung = forms.CharField(widget = forms.Textarea)
