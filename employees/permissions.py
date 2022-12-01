from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsCompanyEmployee(BasePermission):


    def has_object_permission(self, request, view, obj):
        return obj.name == "Employee1" 