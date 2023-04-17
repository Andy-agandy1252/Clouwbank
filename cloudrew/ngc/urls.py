from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('projektai/', views.Projektai, name='projektai'),
    path('projektai/<int:projektas_id>', views.projektas, name='projektas'),
    path('klijentai/', views.Klijentai, name='klijentai'),
    path('darbuotojai/', views.Darbuotojai, name='darbuotojai'),
    path('darbai/', views.Darbai, name='darbai'),
    path('saskaitos/', views.Saskaitos, name='saskaitos'),
]