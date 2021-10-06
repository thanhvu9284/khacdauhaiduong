from django.db import models
from django.utils import timezone
# Create your models here.
from ckeditor.fields import RichTextField

class tintucForm(models.Model):
    tieude = models.CharField("Tiêu đề",max_length=300)
    tomtat = models.TextField("Tóm tắt",max_length=1000)
    noidung = RichTextField("Nội dung",blank=True,null=True)
    hinh = models.ImageField("Hình",blank=True,null=True,upload_to="tintuc/")
    ngaynhap = models.DateTimeField("Ngày nhập",default=timezone.now)
        
    def __str__(self) -> str:
        return self.tieude
    
    class Meta:
        verbose_name = ('Tin tức')
        verbose_name_plural = ("Nội dung Tin tức")