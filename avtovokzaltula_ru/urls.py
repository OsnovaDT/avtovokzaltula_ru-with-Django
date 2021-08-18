"""Urls for folder avtovokzaltula_ru"""

from django.contrib import admin
from django.urls import path, include
import debug_toolbar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', include('bus_stations.urls')),
    path('accounts/', include('accounts.urls')),

    # For VK login
    path(
        'social/',
        include('social_django.urls', namespace='social')
    ),

    # Debug toolbar
    path(
        '__debug__/',
        include(debug_toolbar.urls)
    ),

    # Simple captcha
    path(
        'captcha/',
        include('captcha.urls')
    ),

    # API
    path(
        'api/',
        include('api.urls')
    ),

    # For login and logout in DRF
    path(
        'api-auth/',
        include('rest_framework.urls')
    )
]
