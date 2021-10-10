from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from tintuc.models import tintucForm

def index(request):
    tintuc = tintucForm.objects.all().order_by('-ngaynhap')
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
        
    return render(request, 'tintuc/index.html', context)

def detailNews(request, slug):
    newsall = tintucForm.objects.exclude(slug=slug).order_by('-ngaynhap')[:10]
    contacts = tintucForm.objects.all().filter(slug=slug)
    context = {
        'contacts' : contacts,
        'newsall' : newsall
    }
    
    return render(request, 'tintuc/newsdetail.html', context)