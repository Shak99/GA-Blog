from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('tv/', views.tvshow, name = 'index'),
    path('tv/<int:tv_id>/', views.detail, name = 'detail'),
    path('tv/create', views.TvCreate.as_view(), name='tv_create'),
    path('tv/<int:pk>/update/', views.TvUpdate.as_view(), name='tv_update'),
    path('tv/<int:pk>/delete/', views.TvDelete.as_view(), name='tv_delete'),
]