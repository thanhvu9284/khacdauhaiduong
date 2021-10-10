from django.urls import path
from . import views
app_name = 'service'
urlpatterns = [
    path('', views.indexAll, name='groupservice'),
    path('<slug>/', views.index, name='service'),
    path('<slugn>/<slug>/', views.indexDetail, name='servicedetail')
]
