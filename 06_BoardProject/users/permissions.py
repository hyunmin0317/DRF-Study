from rest_framework import permissions


class CustomReadOnly(permissions.BasePermission):
    # GET: 누구나, PUT/PATCH: 해당 유저
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:  # SAFE_METHODS = GET 과 같은 메소드
            return True
        return obj.user == request.user
