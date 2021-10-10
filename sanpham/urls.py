from django.urls import path
from . import views
app_name = 'product'
urlpatterns = [
    path('', views.index, name='product'),
    path('<slug>/', views.GroupProduct,name='groupproduct'),
    path('<slugn>/<slug>/', views.DetailProduct,name='detailproduct'),
    path('search', views.SearchResult,name='search'),
]
