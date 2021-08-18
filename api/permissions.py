"""Permission classes for ViewSets"""

from rest_framework.permissions import BasePermission, SAFE_METHODS


class SuperUserPermission(BasePermission):
    """Permission class for check that user is superuser"""

    def has_object_permission(self, request, view, obj):
        """Check that user is superuser for the current object"""

        if request.method in SAFE_METHODS:
            return True

        return request.user.is_superuser

    def has_permission(self, request, view):
        """Check that user is superuser for the list of objects"""

        if request.method in SAFE_METHODS:
            return True

        return request.user.is_superuser
