from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.template.defaultfilters import truncatechars
from django.utils.safestring import mark_safe
from django.template.defaultfilters import slugify

# Create your models here.
class NhomSanPham(models.Model):
    """A model of a rock band."""    
    name = models.CharField("Nhóm sản phẩm",max_length=200)
    slug = models.SlugField(('slug'), max_length=200, blank=True,editable=False)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(NhomSanPham, self).save(*args, **kwargs)
        
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name_plural = "Nhóm Sản phẩm"

class SanPham(models.Model):
    """A model of a rock band member."""
    nhomsanpham = models.ForeignKey("NhomSanPham",related_name='children',on_delete=models.CASCADE)
    #nhomsanpham = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name="nhomsanpham")
    tieude = models.CharField("Tên sản phẩm", max_length=500)
    slug = models.SlugField(('slug'), max_length=500, blank=True,editable=False)
    tomtat = models.TextField("Tóm tắt",max_length=1000)
    noidung = RichTextField("Nội dung",blank=True,null=True)
    gia_chinh = models.DecimalField("Giá chinh",max_digits=10,decimal_places = 0,blank=True,null=True)
    gia_khuyenmai = models.DecimalField("Giá khuyến mãi",max_digits=10,decimal_places = 0,blank=True,null=True)
    sp_moi = models.BooleanField("SP mới",blank=True,null=True)
    sp_noibat = models.BooleanField("SP nổi bật",blank=True,null=True)
    sp_khuyenmai = models.BooleanField("SP khuyến mãi",blank=True,null=True)
    hinh = models.FileField("Hình đại diện",blank=True,null=True,upload_to="images/")
    ngaynhap = models.DateTimeField("Ngày nhập",default=timezone.now)   
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.tieude)
        super(SanPham, self).save(*args, **kwargs)
        
    def __str__(self) -> str:
        return self.tieude
       
    @property
    def short_description(self):
        return truncatechars(self.nhomsanpham.name,500)
        short_description.short_description = 'Tên nhóm'
        short_description.allow_tags = True
    
    def admin_photo(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.hinh.url))
        admin_photo.short_description = 'Image'
        admin_photo.allow_tags = True
        
    class Meta:
        verbose_name_plural = "Chi tiết sản phẩm"
        
class SanPhamHinh(models.Model):
    """A model of a rock band member."""
    sanpham = models.ForeignKey(
        "SanPham",
        on_delete=models.CASCADE,
    )
    hinh = models.FileField("Thư viện hình",blank=True,null=True,upload_to="images/")
        
    def __str__(self) -> str:
        return self.sanpham.tieude

    @property
    def short_description(self):
        return truncatechars(self.sanpham.tieude,500)
    
    def admin_photo_detail(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.hinh.url))
        admin_photo_detail.short_description = 'Image'
        admin_photo_detail.allow_tags = True
        
    class Meta:
        verbose_name_plural = "Hình sản phẩm"

class DathangSanPhamModel(models.Model):    
    sanpham = models.ForeignKey(SanPham,on_delete=models.CASCADE)   
    ten = models.CharField("Tên người liên hệ",max_length=150)
    dienthoai = models.CharField("Điện thoại",max_length=50)
    diachi = models.CharField("Địa chỉ",max_length=500)
    soluong = models.IntegerField("Số lượng")
    noidung = models.TextField("Nội dung")    
    ngaynhap = models.DateTimeField("Ngày nhập",default=timezone.now)     
    
    class Meta:
        verbose_name_plural = "Thông tin đặt hàng"
        
class NhanXetSanPhamModel(models.Model):    
    sanpham = models.ForeignKey(SanPham,on_delete=models.CASCADE) 
    ten = models.CharField("Tên người nhận xét",max_length=150)
    email = models.CharField("Email",max_length=50)        
    noidung = models.TextField("Nội dung") 
    ngaynhap = models.DateTimeField("Ngày nhập",default=timezone.now)
    
    class Meta:
        verbose_name_plural = "Thông tin nhận xét"    
                
#class SanPham_Moi_NoiBat(models.Model):   
#    nhomsanpham = models.ForeignKey(NhomSanPham,blank=True,default=None, on_delete = models.CASCADE)
#    sanpham = models.ForeignKey(SanPham,on_delete= models.CASCADE)     
#    kieu = models.SmallIntegerField("Kiểu sản phẩm ",choices=(
#            (1, "Mới"),
#            (2, "Nổi bật"),            
#        )
#    )
#    def __str__(self) -> str:
#        return self.sanpham.tieude
    
#    class Meta:
#        verbose_name_plural = "Sản phẩm mới, nổi bật"