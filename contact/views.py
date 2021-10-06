from django.contrib import messages
from django.shortcuts import  redirect, render
from contact.forms import contact_Form
from contact.models import ContentcontactModel,MapcontactModel,contactModel

def index(request):
    if request.method == 'POST':
        f = contact_Form(request.POST)
        if f.is_valid():
            ten = f.cleaned_data['ten']
            dienthoai = f.cleaned_data['dienthoai']
            email = f.cleaned_data['email']
            noidung = f.cleaned_data['noidung']
            p = contactModel(ten=ten,dienthoai=dienthoai,email=email,noidung=noidung)
            p.save()                            
            result = "Thông tin liên hệ của bạn đã được lưu. Cám ơn bạn đã liên hệ với chúng tôi"           
            messages.success(request, result)          
            return redirect(request.path)

    thongtin_lienhe = ContentcontactModel.objects.all()
    thongtin_map = MapcontactModel.objects.all()
    cf = contact_Form
    
    context = {
        'form':cf,
        'thongtin_lienhe' : thongtin_lienhe,
        'thongtin_map': thongtin_map
    }
    return render(request, 'contact/contact.html', context)