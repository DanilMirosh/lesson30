from django.contrib.auth import get_user_model
from rest_framework import permissions

User = get_user_model()


# TODO напишите здесь необходимые условия в соответствии с заданием
class MarkCreatePermission(permissions.BasePermission):
    message = 'Adding marks for non teacher user not allowed.'

    def has_permission(self, request, view):
        if request.user.role != User.TEACHER:
            return False
        return True
