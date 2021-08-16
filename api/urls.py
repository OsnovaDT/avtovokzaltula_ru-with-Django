"""Urls for API"""

from django.urls import path, include
from rest_framework import routers

from api.views import (
    UserViewSet, BusStationViewSet, RouteViewSet
)


api_router = routers.DefaultRouter()

# First param is slug of api url
api_router.register('users', UserViewSet)
api_router.register('bus_stations', BusStationViewSet)
api_router.register('routes', RouteViewSet)

urlpatterns = [
    path(
        '', include(api_router.urls)
    )
]
