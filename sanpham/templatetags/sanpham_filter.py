from django import template
from sanpham.models import SanPham,SanPhamHinh,NhanXetSanPhamModel

register = template.Library()

@register.filter
def getChilds(id_nhom):
	return SanPham.objects.filter(nhomsanpham_id=id_nhom)

@register.filter
def getChildsImage(id_sanpham):
	return SanPhamHinh.objects.filter(sanpham_id=id_sanpham)

@register.filter
def getCountNhanXet(id_sanpham):
	return NhanXetSanPhamModel.objects.filter(sanpham_id=id_sanpham).count()