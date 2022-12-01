from django.contrib import admin
from django.urls import path, include
from .views import AssetList, AssetDetail


urlpatterns = [
    path('', AssetList.as_view(), name='assets'),
    path('<int:pk>', AssetDetail.as_view(), name='assets'),
    
]