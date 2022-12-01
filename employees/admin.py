from django.contrib import admin

from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'company')

# class EmployeeAssetsAdmin(admin.ModelAdmin):
#     list_display = ('handover_at', 'condition')

admin.site.register(Employee, EmployeeAdmin)
# admin.site.register(EmployeeAssets, EmployeeAssetsAdmin)