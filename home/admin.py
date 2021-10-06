from django.contrib import admin

from .models import homeForm,HomeThuVienHinh,HomeThuVienHinh_ChiTiet,homeHotline

# Register your models here.
admin.site.register(homeHotline)

class homeAdmin(admin.ModelAdmin):
    """Customize the look of the auto-generated admin for the Member model"""
    #list_display = ('title')
    #list_filter = ('username',)

admin.site.register(homeForm,homeAdmin)  # Use the default options

class PostImageAdmin(admin.StackedInline):
    fields = ('hinh','admin_photo_detail')
    list_display = ['admin_photo_detail']
    readonly_fields = ['admin_photo_detail']
    
    model = HomeThuVienHinh_ChiTiet    
 
@admin.register(HomeThuVienHinh)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]
    #fields = ('tieude')
    #list_display = ['tieude']
    #list_display_links=['tieude']
    #list_filter = ['tieude']    
 
    class Meta:
       model = HomeThuVienHinh
 
#@admin.register(SanPhamHinh)
class PostImageAdmin(admin.ModelAdmin):
    pass