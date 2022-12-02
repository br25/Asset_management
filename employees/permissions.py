from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsCompanyEmployee(BasePermission):

    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        return request.user == obj.company.owner
