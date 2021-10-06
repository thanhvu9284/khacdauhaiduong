from django.urls import path
from . import views
app_name = 'bottom'
urlpatterns = [
    path('guarantee/', views.guarantee,name='guarantee'),
    path('sell/', views.sell,name='sell'),
    path('delivery/', views.delivery,name='delivery'),
    path('pay/', views.pay,name='pay'),
    path('buy/', views.buy,name='buy'),
    path('work/', views.work,name='work'),
    path('recruitment/', views.recruitment,name='recruitment'),
]

