"""Urls for API"""

from django.urls import path, include
from rest_framework import routers

from api.views import (
    UserViewSet, BusStationViewSet, RouteViewSet,
    FlightViewSet, BusViewSet, DriverViewSet, TicketViewSet
)


api_router = routers.DefaultRouter()

# First param is slug of api url
api_router.register('users', UserViewSet)
api_router.register('bus_stations', BusStationViewSet)
api_router.register('routes', RouteViewSet)
api_router.register('flights', FlightViewSet)
api_router.register('buses', BusViewSet)
api_router.register('drivers', DriverViewSet)
api_router.register('tickets', TicketViewSet)

urlpatterns = [
    path(
        '', include(api_router.urls)
    )
]
