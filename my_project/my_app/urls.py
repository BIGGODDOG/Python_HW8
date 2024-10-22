from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('table/', views.multiplication_table, name='table'),
    path('programmer_day/', views.programmer_day, name='programmer_day'),
]