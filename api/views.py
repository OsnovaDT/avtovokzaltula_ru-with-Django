"""Views for folder api"""

from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from bus_stations.models import (
    BusStation, Route, Flight, Bus, Driver, Ticket
)
from api.permissions import SuperUserPermission
from api.serializers import (
    UserSerializer, BusStationSerializer, RouteSerializer,
    FlightSerializer, BusSerializer, DriverSerializer, TicketSerializer
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
    """ViewSet for Route model"""

    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    permission_classes = (
        IsAuthenticatedOrReadOnly, SuperUserPermission
    )


class FlightViewSet(ModelViewSet):
    """ViewSet for Flight model"""

    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = (
        IsAuthenticatedOrReadOnly, SuperUserPermission
    )


class BusViewSet(ModelViewSet):
    """ViewSet for Bus model"""

    queryset = Bus.objects.all()
    serializer_class = BusSerializer
    permission_classes = (
        IsAuthenticatedOrReadOnly, SuperUserPermission
    )


class DriverViewSet(ModelViewSet):
    """ViewSet for Driver model"""

    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    permission_classes = (
        IsAuthenticatedOrReadOnly, SuperUserPermission
    )


class TicketViewSet(ModelViewSet):
    """ViewSet for Ticket model"""

    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = (
        IsAuthenticatedOrReadOnly, SuperUserPermission
    )
