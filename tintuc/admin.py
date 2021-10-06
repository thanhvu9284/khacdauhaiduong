from django.contrib import admin

from .models import tintucForm
# Register your models here.
class tintucAdmin(admin.ModelAdmin):
    """Customize the look of the auto-generated admin for the Member model"""
    list_display = ('tieude','ngaynhap')
    #list_filter = ('username',)

admin.site.register(tintucForm,tintucAdmin)  # Use the default options