from django.db import models
from ckeditor.fields import RichTextField

class contactModel(models.Model):
    ten = models.CharField("Tên người liên hệ",max_length=150)
    dienthoai = models.CharField("Điện thoại",max_length=50)
    email = models.EmailField("Email")
    noidung = RichTextField(blank=True,null=True)    

    class Meta:
        verbose_name_plural = "Thông tin người liên hệ"
    
class MapcontactModel(models.Model):
    title = models.CharField("Bản đồ",max_length=500)    
    body = RichTextField(blank=True,null=True)    

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Bản đồ liên hệ"

class ContentcontactModel(models.Model):
    title = models.CharField("Nội dung liên hệ",max_length=500)    
    body = RichTextField(blank=True,null=True)    

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Nội dung liên hệ"