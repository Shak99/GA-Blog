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
    path('tv/<int:tv_id>/add_studio/', views.add_studio, name='add_studio'),
    path('tv/<int:tv_id>/assoc_tvhost/<int:tvhost_id>/', views.assoc_tvhost, name='assoc_tvhost'),
    
    # path('tv/<int:tv_id>/add_platform/', views.PlatformCreate().as_view(), name='add_platform'),
    
    path('tvhost/create', views.TvHostCreate.as_view(), name = 'tvhost_create'),
     path('tvhost/', views.TvHostList.as_view(), name='tvhost_index'),
    # path('platform/<int:pk>', views.PlatformDetail.as_view(), name='tvplatform_detail'),
    # path('platform/<int:pk/update/', views.PlatformUpdate.as_view(), name='tvplatform_update'),
    # path('platform/<int:pk/delete/', views.PlatformDelete.as_view(), name='tvplatform_delete'),
    
]