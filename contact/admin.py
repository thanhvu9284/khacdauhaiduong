from django.contrib import admin
from .models import contactModel
from .models import MapcontactModel
from .models import ContentcontactModel

class MapcontactFormAdmin(admin.ModelAdmin):
    """Customize the look of the auto-generated admin for the Member model"""
    #list_display = ('title')
    #ist_filter = ('title')
    
admin.site.register(MapcontactModel, MapcontactFormAdmin)

class ContentcontactFormAdmin(admin.ModelAdmin):
    """Customize the look of the auto-generated admin for the Member model"""
    #list_display = ('title')
    
admin.site.register(ContentcontactModel,ContentcontactFormAdmin)

class MemberAdmin(admin.ModelAdmin):
    """Customize the look of the auto-generated admin for the Member model"""
    list_display = ('ten','dienthoai', 'email')
    #list_filter = ('username')

admin.site.register(contactModel,MemberAdmin)  # Use the default options