from rest_framework import permissions

"""
Allow unsafe methods for staff users only.
"""
class IsStaffOrReadOnly(permissions.BasePermission):
    
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if not request.user or not request.user.is_authenticated():
            return False
        if request.user.is_staff:
            return True
        return False

"""
Custom permissions for the Chapter Model

List/Detail - Public Permission
Create - Authenticated Permission
Update/Delete - Owner or Staff Permission
"""
class ChapterPermissions(permissions.BasePermission):
    
    def has_permission(self, request, view):
        # always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_staff:
            return True
        if request.user.is_authenticated():
            return True
        return False
    
    
    """Object permissions only run if global permissions evaluate to True"""    
    def has_object_permission(self, request, view, obj):
        # always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_staff:
            return True
        if request.user.is_authenticated() and request.method == 'POST':
            return True
        if obj.owner == request.user:
            return True
        return False