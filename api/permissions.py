"""Permission classes for ViewSets"""

from rest_framework.permissions import BasePermission, SAFE_METHODS


def is_user_has_permission_for_action(request):
    """True if user has permission to do the action and False else"""

    if request.method in SAFE_METHODS:
        return True

    return request.user.is_superuser


class SuperUserPermission(BasePermission):
    """Permission class for check that user is superuser"""

    def has_object_permission(self, request, view, obj):
        """Check that user is superuser for the current object"""

        return is_user_has_permission_for_action(request)

    def has_permission(self, request, view):
        """Check that user is superuser for the list of objects"""

        return is_user_has_permission_for_action(request)
