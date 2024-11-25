from django.urls import path
from . import views

urlpatterns = [
    path('', views.funcao_criada_na_views, name='nome_do_link'),
    path('nome_caminho_url/', views.funcao_criada_na_views, name='nome_do_link'),
]
