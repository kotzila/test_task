from rest_framework import permissions


class CustomPermission(permissions.BasePermission):
    """
    Custom permission to only allow admin3 to edit it.
    """

    def has_permission(self, request, view):
        """
        Return `True` if permission is granted, `False` otherwise.
        """

        # Read permissions are allowed to any request,
        #  so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.username == 'admin3'