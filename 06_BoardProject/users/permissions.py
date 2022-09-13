from rest_framework import permissions


# GET: 누구나, PUT/PATCH: 해당 유저
class CustomReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:  # 데이터 영향 X (GET)
            return True
        return obj.user == request.user
