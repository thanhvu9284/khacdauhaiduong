from django import forms
from ckeditor.fields import RichTextField

class gioithieuForm(forms.Form):
    title = forms.CharField(blank=True,null=True)
    body = RichTextField(blank=True,null=True)