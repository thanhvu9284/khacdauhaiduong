from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.template.defaultfilters import truncatechars
from django.utils.safestring import mark_safe

class homeForm(models.Model):
    title = models.CharField("Tiêu đề",max_length=200,blank=True,null=True)
    body = RichTextUploadingField(blank=True,null=True)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = ('Trang chủ')
        verbose_name_plural = ("Nội dung Trang chủ")
        
class HomeThuVienHinh(models.Model):
    tieude = models.CharField("Tiêu đề", max_length=500)
    
    def __str__(self) -> str:
        return self.tieude
    
    @property
    def short_description(self):
        return truncatechars(self.tieude,500)

    class Meta:
        verbose_name_plural = "LiveShow hình trang chủ"
        
class HomeThuVienHinh_ChiTiet(models.Model):
    """A model of a rock band member."""
    homethuvienhinh = models.ForeignKey(
        "HomeThuVienHinh",
        on_delete=models.CASCADE,
    )
    hinh = models.FileField("Thư viện hình",blank=True,null=True,upload_to="imagesHome/")
        
    def __str__(self) -> str:
        return self.homethuvienhinh.tieude
    
    @property
    def short_description(self):
        return truncatechars(self.homethuvienhinh.tieude,500)
    
    def admin_photo_detail(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.hinh.url))
        admin_photo_detail.short_description = 'Image'
        admin_photo_detail.allow_tags = True
        
    class Meta:
        verbose_name_plural = "Hình chi tiết"
        
class homeHotline(models.Model):
    title = models.CharField("Hotline",max_length=100,blank=True,null=True)    

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name_plural = ("Hotline")