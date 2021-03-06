from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product/<str:pk>/', views.product, name='product'),
    path('search/', views.search, name='search')
]