from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone

# Create your models here.
class NhomDichVu(models.Model):
    """A model of a rock band."""    
    name = models.CharField("Nhóm dịch vụ",max_length=200)
    
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
    tomtat = models.TextField("Tóm tắt",max_length=1000)
    noidung = RichTextField("Nội dung",blank=True,null=True)
    hinh = models.ImageField("Hình",blank=True,null=True,upload_to="dichvu/")
    ngaynhap = models.DateTimeField("Ngày nhập",default=timezone.now)   
    
    def __str__(self) -> str:
        return self.tieude
    
    class Meta:
        verbose_name_plural = "Chi tiết dịch vụ"