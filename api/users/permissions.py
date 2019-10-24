from rest_framework import permissions


class IsAdminOrOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_admin or obj.owner == request.user


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.owner == request.user


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return request.user.is_admin


class IsAdminOrCreateOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in ('POST', ):
            return True
        else:
            return bool(request.user.is_authenticated and request.user.is_admin)
