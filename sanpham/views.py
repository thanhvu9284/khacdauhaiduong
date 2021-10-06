from django.utils import timezone
from sanpham.forms import DathangSanPham_Form,NhanXet_Form
from sanpham.models import SanPham,NhomSanPham,DathangSanPhamModel,NhanXetSanPhamModel
from django.shortcuts import redirect, render
from django.contrib import messages

def index(request):
    nhomsanpham =  NhomSanPham.objects.all().order_by("name")
    
    return render(request, 'sanpham/index.html', {'nhomsanpham': nhomsanpham} )

def GroupProduct(request, id):    
    nhomsanpham =  NhomSanPham.objects.filter(id=id)
    contacts = SanPham.objects.all().filter(nhomsanpham=id)
    context = {
        'nhomsanpham' : nhomsanpham,
        'contacts' : contacts,        
    }
    
    return render(request, 'sanpham/groupproduct.html', context)

def DetailProduct(request,idn,id):
    if request.method == 'POST':
        if 'btn_nhanxet' in request.POST:
            f = NhanXet_Form(request.POST)           
            if f.is_valid():
                ten = f.cleaned_data['ten']                                     
                email = f.cleaned_data['email']
                noidung = f.cleaned_data['noidung']        
                a = SanPham.objects.get(id=id)    
                NhanXetSanPhamModel(ten=ten,email=email,noidung=noidung,sanpham=a).save()
                        
                result = "Nhận xét của bạn đã được lưu."                       
                messages.success(request, result)          
                return redirect(request.path)
        
        if 'btn_dathang' in request.POST:
            f = DathangSanPham_Form(request.POST)
            if f.is_valid():
                ten = f.cleaned_data['ten']
                dienthoai = f.cleaned_data['dienthoai']
                diachi = f.cleaned_data['diachi']
                soluong = f.cleaned_data['soluong']
                noidung = f.cleaned_data['noidung']        
                a = SanPham.objects.get(id=id)    
                DathangSanPhamModel(ten=ten,dienthoai=dienthoai,diachi=diachi,soluong=soluong,noidung=noidung,sanpham=a).save()
                            
                result = "Thông tin đặt hàng của bạn đã được lưu. Chúng tôi sẽ liên hệ với bạn trong thời gian sớm nhất"                       
                messages.success(request, result)          
                return redirect(request.path)
        
    nhomsanpham = NhomSanPham.objects.all().filter(id=idn)
    groupproduct = SanPham.objects.filter(nhomsanpham__id=idn).exclude(id=id).order_by('tieude')
    contacts = SanPham.objects.all().filter(id=id)
    cf = DathangSanPham_Form
    ct_nx = NhanXet_Form
    context = {
        'form':cf,
        'form_nx':ct_nx,
        'contacts' : contacts,
        'groupproduct' : groupproduct,
        'nhomsanpham' : nhomsanpham
    }
    
    return render(request, 'sanpham/detailproduct.html', context)

def SearchResult(request):
    q = request.POST['search']
    contacts = SanPham.objects.filter(tieude__contains=q)
    return render(request, 'sanpham/searchresult.html', {'contacts':contacts} )