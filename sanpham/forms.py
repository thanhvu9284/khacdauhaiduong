from django import forms
from django.forms import widgets
from django.forms.fields import EmailField

class DathangSanPham_Form(forms.Form):
    ten = forms.CharField(max_length=150)
    dienthoai = forms.CharField(max_length=50)
    diachi = forms.CharField(max_length=350)
    soluong = forms.CharField(max_length=50)
    noidung = forms.CharField(widget = forms.Textarea)
    
class NhanXet_Form(forms.Form):
    ten = forms.CharField(max_length=150)    
    email = forms.CharField(max_length=50)   
    noidung = forms.CharField(widget = forms.Textarea)