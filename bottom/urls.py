from django.urls import path
from . import views
app_name = 'bottom'
urlpatterns = [
    path('bao-hanh-va-doi-tra/', views.guarantee,name='bao-hanh-va-doi-tra'),
    path('chinh-sach-ban-hang/', views.sell,name='chinh-sach-ban-hang'),
    path('chinh-sach-giao-hang/', views.delivery,name='chinh-sach-giao-hang'),
    path('quy-dinh-va-hinh-thuc-thanh-toan/', views.pay,name='quy-dinh-va-hinh-thuc-thanh-toan'),
    path('huong-dan-mua-hang/', views.buy,name='huong-dan-mua-hang'),
    path('quy-che-hoat-dong/', views.work,name='quy-che-hoat-dong'),
    path('tuyen-dung/', views.recruitment,name='tuyen-dung'),
]

