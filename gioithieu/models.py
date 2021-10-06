from django.db import models

# Create your models here.
from ckeditor.fields import RichTextField

class gioithieuForm(models.Model):
    title = models.CharField("Tiêu đề",max_length=200,blank=True,null=True)
    body = RichTextField(blank=True,null=True)
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = ('Giới thiệu')
        verbose_name_plural = ("Nội dung Giới thiệu")