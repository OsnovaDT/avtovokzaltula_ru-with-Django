from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', include('bus_stations.urls')),
    path('accounts/', include('accounts.urls')),

    # For VK login
    path(
        'social/',
        include('social_django.urls', namespace='social')
    )
]
