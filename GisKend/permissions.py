from django.conf import settings
from rest_framework.permissions import BasePermission

class Authentication(BasePermission):
    def has_permission(self, request, view):
        # API_KEY should be in request headers to authenticate requests
        api_key_secret = request.META.get('HTTP_AUTHENTICATION')
        return api_key_secret == settings.API_KEY_SECRET