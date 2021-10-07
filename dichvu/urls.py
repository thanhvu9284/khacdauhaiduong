from django.urls import path
from . import views
app_name = 'service'
urlpatterns = [
    path('', views.indexAll, name='groupservice'),
    path('<int:id>/', views.index, name='service'),
    path('<int:idn>/<int:id>/', views.indexDetail, name='servicedetail')
]
