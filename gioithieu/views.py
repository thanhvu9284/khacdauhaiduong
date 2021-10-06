from django.shortcuts import render
from gioithieu.models import gioithieuForm

def index(request):
    gioithieu= gioithieuForm.objects.all()
    return render(request, 'gioithieu/index.html', {'gioithieu': gioithieu})