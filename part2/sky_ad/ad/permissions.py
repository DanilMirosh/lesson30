from rest_framework import permissions


# TODO напишите здесь необходимые условия в соответствии с заданием
class AdUpdatePermission(permissions.BasePermission):
    message = 'Updating not your add is not permitted'

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if hasattr(obj, "user"):
            return request.user and request.user.is_authenticated and obj.user == request.user
        else:
            return request.user and request.user.is_authenticated and obj.user == request.user
