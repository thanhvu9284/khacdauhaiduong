"""khacdauhaiduong URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls'),name='home'),
    path('post/', include('post.urls'),name='post'),
    path('contact/', include('contact.urls'),name='contact'),    
    path('about/', include('gioithieu.urls'),name='about'),
    path('news/', include('tintuc.urls'),name='news'),
    path('news/<int:id>/', include('tintuc.urls'),name='newsdetail'),
    path('service/', include('dichvu.urls'),name='service'),
    path('service/<int:id>/', include('dichvu.urls'),name='groupservice'),
    path('service/<int:idn>/<int:id>/', include('dichvu.urls'),name='detailservice'),
    path('product/', include('sanpham.urls'),name='product'),
    path('product/<int:id>/', include('sanpham.urls'),name='groupproduct'),
    path('guarantee/', include('bottom.urls'),name='guarantee'),
    path('sell/', include('bottom.urls'),name='sell'),
    path('delivery/', include('bottom.urls'),name='delivery'),
    path('pay/', include('bottom.urls'),name='pay'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header="Trang quản trị thông tin"
admin.site.index_title="Trang quản trị thông tin"
admin.site.site_title="Trang quản trị thông tin"