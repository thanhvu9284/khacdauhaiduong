from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from dichvu.models import DichVu,NhomDichVu

def index(request, id):
    tintuc = DichVu.objects.filter(nhomdichvu=id).order_by('-ngaynhap')
    #tintuc = DichVu.objects.all().order_by('-ngaynhap')
    paginator = Paginator(tintuc, 10)
    page_number = request.GET.get("page")
    try:
        contacts = paginator.page(page_number)
    except PageNotAnInteger:
        # Nếu page_number không thuộc kiểu integer, trả về page đầu tiên
        contacts = paginator.page(1)
    except EmptyPage:
        # Nếu page không có item nào, trả về page cuối cùng
        contacts = paginator.page(paginator.num_pages)
    
    context = {
        'contacts' : contacts
    }
        
    return render(request, 'dichvu/index.html', context)

def indexDetail(request, idn, id):
    nhomdichvu = NhomDichVu.objects.filter(id=idn)
    dichvu = DichVu.objects.filter(id=id)
    alldichvu = DichVu.objects.all()

    context = {
        'nhomdichvu' : nhomdichvu,
        'dichvu' : dichvu,
        'alldichvu' : alldichvu,
    }
        
    return render(request, 'dichvu/servicedetail.html', context)