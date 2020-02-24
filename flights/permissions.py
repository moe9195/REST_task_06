from rest_framework.permissions import BasePermission
import datetime

class IsUser(BasePermission):
    message = "You must be the owner of the booking to access this page."

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or (obj.user == request.user):
            return True
        else:
            return False

class IsWithinTime(BasePermission):
    message = "Your booking date is too close to cancel."

    def has_object_permission(self, request, view, obj):
        if (obj.date - datetime.date.today()).days < 3:
            return False
        else:
            return True
