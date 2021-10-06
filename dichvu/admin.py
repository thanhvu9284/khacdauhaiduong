import dichvu
from django.contrib import admin

# Register your models here.
from dichvu.models import NhomDichVu,DichVu

class MemberAdmin(admin.ModelAdmin):
    """Customize the look of the auto-generated admin for the Member model"""
    #list_display = ('name')
    #list_filter = ('name',)

admin.site.register(NhomDichVu)  # Use the default options
admin.site.register(DichVu, MemberAdmin)  # Use the customized options