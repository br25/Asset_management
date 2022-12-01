from django.contrib import admin
from django.urls import path, include
from .views import EmployeeList, EmployeeDetail


urlpatterns = [
    path('', EmployeeList.as_view(), name='employees'),
    path('<int:pk>', EmployeeDetail.as_view(), name='employees-detail')
]