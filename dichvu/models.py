from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.template.defaultfilters import slugify

# Create your models here.
class NhomDichVu(models.Model):
    """A model of a rock band."""    
    name = models.CharField("Nhóm dịch vụ",max_length=200)
    slug = models.SlugField(('slug'), max_length=200, blank=True,editable=False)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(NhomDichVu, self).save(*args, **kwargs)
        
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name_plural = "Nhóm Dịch vụ"

class DichVu(models.Model):
    """A model of a rock band member."""
    nhomdichvu = models.ForeignKey(
        "NhomDichVu",
        on_delete=models.CASCADE,
    )
    tieude = models.CharField("Tên dịch vụ", max_length=500)
    slug = models.SlugField(('slug'), max_length=500, blank=True,editable=False)
    tomtat = models.TextField("Tóm tắt",max_length=1000)
    noidung = RichTextField("Nội dung",blank=True,null=True)
    hinh = models.ImageField("Hình",blank=True,null=True,upload_to="dichvu/")
    ngaynhap = models.DateTimeField("Ngày nhập",default=timezone.now)   
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.tieude)
        super(DichVu, self).save(*args, **kwargs)
        
    def __str__(self) -> str:
        return self.tieude
    
    class Meta:
        verbose_name_plural = "Chi tiết dịch vụ"