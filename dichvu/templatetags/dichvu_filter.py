from django import template
from dichvu.models import NhomDichVu

register = template.Library()

@register.filter
def getSlugNhomDichVu(id_nhom):
	return NhomDichVu.objects.filter(id=id_nhom)