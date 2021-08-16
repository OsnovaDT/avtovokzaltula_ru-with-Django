"""Views for folder api"""

from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet

from bus_stations.models import BusStation, Route
from api.serializers import (
    UserSerializer, BusStationSerializer, RouteSerializer
)


class UserViewSet(ModelViewSet):
    """ViewSet for User model"""

    queryset = User.objects.all()
    serializer_class = UserSerializer


class BusStationViewSet(ModelViewSet):
    """ViewSet for BusStation model"""

    queryset = BusStation.objects.all()
    serializer_class = BusStationSerializer


class RouteViewSet(ModelViewSet):
    """ViewSet Route User model"""

    queryset = Route.objects.all()
    serializer_class = RouteSerializer
