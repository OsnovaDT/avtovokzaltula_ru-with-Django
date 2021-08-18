"""Urls for API"""

from django.urls import path, include
from rest_framework import routers

from api.views import (
    UserViewSet, BusStationViewSet, RouteViewSet,
    FlightViewSet, BusViewSet, DriverViewSet, TicketViewSet
)

# Slug will set after .../api/
SLUG_AND_VIEWSET = {
    'users': UserViewSet,
    'bus_stations': BusStationViewSet,
    'routes': RouteViewSet,
    'flights': FlightViewSet,
    'buses': BusViewSet,
    'drivers': DriverViewSet,
    'tickets': TicketViewSet,
}


api_router = routers.DefaultRouter()

for slug, view_set in SLUG_AND_VIEWSET.items():
    api_router.register(slug, view_set)


urlpatterns = [
    path(
        '', include(api_router.urls)
    )
]
