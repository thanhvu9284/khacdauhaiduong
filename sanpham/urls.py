from django.urls import path
from . import views
app_name = 'product'
urlpatterns = [
    path('', views.index, name='product'),
    path('<int:id>/', views.GroupProduct,name='groupproduct'),
    path('<int:idn>/<int:id>/', views.DetailProduct,name='detailproduct'),
    path('search', views.SearchResult,name='search'),
]
