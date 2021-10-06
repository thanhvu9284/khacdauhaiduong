from home.models import homeForm,HomeThuVienHinh_ChiTiet
from django.shortcuts import render
from sanpham.models import SanPham 
from bottom.models import cl_bottom

def index(request):
    thuvienhinh = HomeThuVienHinh_ChiTiet.objects.all()
    home_content = homeForm.objects.all()  
    
    context = {
        'thuvienhinh': thuvienhinh,'home_content': home_content
    }
    
    
    return render(request, 'home/index.html',  context)
    
