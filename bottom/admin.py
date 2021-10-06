from django.contrib import admin
from .models import cl_bottom,cl_baohanh_doitra,cl_chinhsach_banhang,cl_chinhsach_giaohang,cl_quydinh_thanhtoan,cl_huongdanmuahang,cl_quychehoatdong,cl_tuyendung

class cl_bottomAdmin(admin.ModelAdmin):
    """Customize the look of the auto-generated admin for the Member model"""
    #list_display = ('title')
    #ist_filter = ('title')
    
admin.site.register(cl_bottom, cl_bottomAdmin)
admin.site.register(cl_baohanh_doitra)
admin.site.register(cl_chinhsach_banhang)
admin.site.register(cl_chinhsach_giaohang)
admin.site.register(cl_quydinh_thanhtoan)
admin.site.register(cl_huongdanmuahang)
admin.site.register(cl_quychehoatdong)
admin.site.register(cl_tuyendung)