from django.contrib import admin
from django.urls import path, include
from .views import AssetList, AssetDetail, DelegateAsset


urlpatterns = [
    path('', AssetList.as_view(), name='assets'),
    path('<int:pk>', AssetDetail.as_view(), name='assets_detail'),
    path('<int:pk>/delegate', DelegateAsset.as_view(), name='delegate_asset'),
    
]
