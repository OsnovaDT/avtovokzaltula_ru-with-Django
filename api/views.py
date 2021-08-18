"""Views for folder api"""

from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from bus_stations.models import BusStation, Route
from api.permissions import SuperUserPermission
from api.serializers import (
    UserSerializer, BusStationSerializer, RouteSerializer,
)


class UserViewSet(ModelViewSet):
    """ViewSet for User model"""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (
        IsAuthenticatedOrReadOnly, SuperUserPermission
    )


class BusStationViewSet(ModelViewSet):
    """ViewSet for BusStation model"""

    queryset = BusStation.objects.all()
    serializer_class = BusStationSerializer
    permission_classes = (
        IsAuthenticatedOrReadOnly, SuperUserPermission
    )


class RouteViewSet(ModelViewSet):
    """ViewSet Route User model"""

    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    permission_classes = (
        IsAuthenticatedOrReadOnly, SuperUserPermission
    )
