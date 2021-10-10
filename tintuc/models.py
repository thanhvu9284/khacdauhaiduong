from django.db import models
from django.utils import timezone
# Create your models here.
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify

class tintucForm(models.Model):
    tieude = models.CharField("Tiêu đề",max_length=300)
    slug = models.SlugField(('slug'), max_length=300, blank=True,editable=False)
    tomtat = models.TextField("Tóm tắt",max_length=1000)
    noidung = RichTextField("Nội dung",blank=True,null=True)
    hinh = models.ImageField("Hình",blank=True,null=True,upload_to="tintuc/")
    ngaynhap = models.DateTimeField("Ngày nhập",default=timezone.now)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.tieude)
        super(tintucForm, self).save(*args, **kwargs)
        
    def __str__(self) -> str:
        return self.tieude
    
    class Meta:
        verbose_name = ('Tin tức')
        verbose_name_plural = ("Nội dung Tin tức")