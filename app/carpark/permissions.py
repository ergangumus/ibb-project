from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsSuperUserOrReadOnly(BasePermission):
    """
    Custom permission to only allow superusers to edit or delete objects.
    """
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            # Read permissions are allowed for any request
            return True
        # Write permissions are only allowed to superusers
        return request.user and request.user.is_superuser
