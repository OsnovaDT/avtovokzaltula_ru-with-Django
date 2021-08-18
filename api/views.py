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


class AdminPermissionMixin(ModelViewSet):
    """Mixin for admin permission"""

    permission_classes = (
        IsAuthenticatedOrReadOnly, SuperUserPermission
    )


class UserViewSet(AdminPermissionMixin):
    """ViewSet for User model"""

    queryset = User.objects.all()
    serializer_class = UserSerializer


class BusStationViewSet(AdminPermissionMixin):
    """ViewSet for BusStation model"""

    queryset = BusStation.objects.all()
    serializer_class = BusStationSerializer


class RouteViewSet(AdminPermissionMixin):
    """ViewSet for Route model"""

    queryset = Route.objects.all()
    serializer_class = RouteSerializer


class FlightViewSet(AdminPermissionMixin):
    """ViewSet for Flight model"""

    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


class BusViewSet(AdminPermissionMixin):
    """ViewSet for Bus model"""

    queryset = Bus.objects.all()
    serializer_class = BusSerializer


class DriverViewSet(AdminPermissionMixin):
    """ViewSet for Driver model"""

    queryset = Driver.objects.all()
    serializer_class = DriverSerializer


class TicketViewSet(AdminPermissionMixin):
    """ViewSet for Ticket model"""

    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
