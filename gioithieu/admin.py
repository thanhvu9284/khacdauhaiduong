from django.contrib import admin

from .models import gioithieuForm
# Register your models here.
class gioithieuAdmin(admin.ModelAdmin):
    """Customize the look of the auto-generated admin for the Member model"""
    #list_display = ('title')
    #list_filter = ('username',)

admin.site.register(gioithieuForm,gioithieuAdmin)  # Use the default options