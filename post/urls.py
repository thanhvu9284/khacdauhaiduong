from django.urls import path
from . import views
app_name = 'post'
urlpatterns = [
    path('', views.post,name='post'),
    path('/1', views.post1),
    path('/2', views.post2)
]
