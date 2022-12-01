from django.contrib import admin

from .models import User, Company

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff')

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'domain', 'owner')

admin.site.register(User, UserAdmin)
admin.site.register(Company, CompanyAdmin)