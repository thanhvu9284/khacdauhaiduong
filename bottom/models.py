from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class cl_bottom(models.Model):   
    body = RichTextField(blank=True,null=True)    
    
    class Meta:
        verbose_name_plural = "Nội dung Bottom"
        
class cl_baohanh_doitra(models.Model):   
    body = RichTextUploadingField(blank=True,null=True)
    
    class Meta:
        verbose_name_plural = "Bảo hành & đổi trả"
        
class cl_chinhsach_banhang(models.Model):   
    body = RichTextUploadingField(blank=True,null=True)
    
    class Meta:
        verbose_name_plural = "Chính sách bán hàng"
    
class cl_chinhsach_giaohang(models.Model):   
    body = RichTextUploadingField(blank=True,null=True)
    
    class Meta:
        verbose_name_plural = "Chính sách giao hàng"
        
class cl_quydinh_thanhtoan(models.Model):   
    body = RichTextUploadingField(blank=True,null=True)
    
    class Meta:
        verbose_name_plural = "Quy định & hình thức thanh toán"
        
class cl_huongdanmuahang(models.Model):   
    body = RichTextUploadingField(blank=True,null=True)
    
    class Meta:
        verbose_name_plural = "Hướng dẫn mua hàng"
        
class cl_quychehoatdong(models.Model):   
    body = RichTextUploadingField(blank=True,null=True)
    
    class Meta:
        verbose_name_plural = "Quy chế hoạt động"

class cl_tuyendung(models.Model):   
    body = RichTextUploadingField(blank=True,null=True)
    
    class Meta:
        verbose_name_plural = "Tuyển dụng"