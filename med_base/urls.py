from django.urls import path
from . import views


app_name = 'med'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
]
