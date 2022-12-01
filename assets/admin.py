from django.contrib import admin

from .models import Asset

class AssetAdmin(admin.ModelAdmin):
    list_display = ('title', 'types', 'is_assigned')


admin.site.register(Asset, AssetAdmin)