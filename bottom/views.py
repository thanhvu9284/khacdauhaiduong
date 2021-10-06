from django.shortcuts import render
from bottom.models import cl_baohanh_doitra,cl_chinhsach_banhang,cl_chinhsach_giaohang,cl_quydinh_thanhtoan

def guarantee(request):
    content= cl_baohanh_doitra.objects.all()
    return render(request, 'bottom/baohanh.html', {'content': content})

def sell(request):
    content= cl_chinhsach_banhang.objects.all()
    return render(request, 'bottom/chinhsachbanhang.html', {'content': content})

def delivery(request):
    content= cl_chinhsach_giaohang.objects.all()
    return render(request, 'bottom/chinhsachgiaohang.html', {'content': content})

def pay(request):
    content= cl_quydinh_thanhtoan.objects.all()
    return render(request, 'bottom/quydinhhinhthucthanhtoan.html', {'content': content})

def buy(request):
    content= cl_quydinh_thanhtoan.objects.all()
    return render(request, 'bottom/huongdanmuahang.html', {'content': content})

def work(request):
    content= cl_quydinh_thanhtoan.objects.all()
    return render(request, 'bottom/quychehoatdong.html', {'content': content})

def recruitment(request):
    content= cl_quydinh_thanhtoan.objects.all()
    return render(request, 'bottom/tuyendung.html', {'content': content})