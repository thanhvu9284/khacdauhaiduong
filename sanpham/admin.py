from django.contrib import admin
from django.forms.models import ModelChoiceField
from sanpham.models import NhomSanPham, SanPham, SanPhamHinh, DathangSanPhamModel,NhanXetSanPhamModel

class NhomSanPhamAdmin(admin.ModelAdmin):
    """Customize the look of the auto-generated admin for the Member model"""

admin.site.register(NhomSanPham,NhomSanPhamAdmin)  # Use the default options

#class SanPham_Moi_NoiBatAdmin(admin.ModelAdmin):
#    """Customize the look of the auto-generated admin for the Member model"""
    #fields = ('tieude','kieu')
    #list_display = ['tieude','kieu']
    #list_filter = ['kieu']    
    
    
#admin.site.register(SanPham_Moi_NoiBat,SanPham_Moi_NoiBatAdmin)

class PostImageAdmin(admin.StackedInline):
    fields = ('hinh','admin_photo_detail')
    list_display = ['admin_photo_detail']
    readonly_fields = ['admin_photo_detail']    
    model = SanPhamHinh    

@admin.register(SanPham)

class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]
    fields = ('tieude','tomtat','noidung','hinh','admin_photo','gia_chinh','gia_khuyenmai','sp_moi','sp_noibat','sp_khuyenmai')
    list_display = ['admin_photo','tieude','gia_chinh','gia_khuyenmai','sp_moi','sp_noibat','sp_khuyenmai']
    list_display_links=['tieude']
    list_filter = ['nhomsanpham__name']
    readonly_fields = ['admin_photo','short_description']
 
    class Meta:
       model = SanPham
 
class PostImageAdmin(admin.ModelAdmin):
    pass

class DathangSanPhamModelAdmin(admin.ModelAdmin):
    list_display = ['ten','dienthoai','diachi','soluong','noidung','ngaynhap']
    #list_filter = ['sanpham__tieude']

admin.site.register(DathangSanPhamModel,DathangSanPhamModelAdmin)

class NhanXetSanPhamModelAdmin(admin.ModelAdmin):
    list_display = ['ten','email','noidung','ngaynhap']
    #list_filter = ['sanpham__tieude']

admin.site.register(NhanXetSanPhamModel,NhanXetSanPhamModelAdmin)