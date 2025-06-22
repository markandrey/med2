from django.urls import path
from . import views


app_name = 'patients'

urlpatterns = [
    path('', views.get_patients, name='index'),
    path('case/', views.case_history, name='case_history'),
]
