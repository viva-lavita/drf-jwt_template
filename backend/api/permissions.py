from rest_framework.permissions import BasePermission


class AuthorOrStaff(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            return obj.id == request.user.id or request.user.is_staff


class NotIsAuthenticated(BasePermission):
    def has_permission(self, request, view):
        return not request.user.is_authenticated
