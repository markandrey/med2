from django.urls import path
from . import views


app_name = 'tests_and_observs'

urlpatterns = [
    path('tests/', views.test_list, name='test_list'),
    path('tests/<int:id>/', views.one_test, name='one_test'),
]
