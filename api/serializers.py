"""Serializers for API"""

from django.contrib.auth.models import User
from rest_framework.serializers import (
    HyperlinkedModelSerializer, StringRelatedField,
    ReadOnlyField
)

from bus_stations.models import (
    BusStation, Route, Flight, Bus, Driver, Ticket
)


class UserSerializer(HyperlinkedModelSerializer):
    """Serializer for model User"""

    class Meta:
        """Choose model User and it's fields"""

        model = User
        fields = (
            'username', 'first_name',
            'last_name', 'email', 'url'
        )


class BusStationSerializer(HyperlinkedModelSerializer):
    """Serializer for model BusStation"""

    routes = StringRelatedField(
        many=True, read_only=True
    )

    class Meta:
        """Choose model BusStation and it's fields"""

        model = BusStation
        fields = (
            'name', 'routes', 'address', 'phone_number',
            'office_hours', 'url'
        )


class RouteSerializer(HyperlinkedModelSerializer):
    """Serializer for model Route"""

    bus_station_name = ReadOnlyField(source='bus_station.name')
    flights = StringRelatedField(many=True, read_only=True)

    class Meta:
        """Choose model Route and it's fields"""

        model = Route
        fields = (
            'name', 'flights', 'regularity', 'departure_time',
            'price', 'bus_station_name', 'bus_station', 'url'
        )


class FlightSerializer(HyperlinkedModelSerializer):
    """Serializer for model Flight"""

    route_name = ReadOnlyField(source='route.name')
    bus_registration_number = ReadOnlyField(source='bus.registration_number')

    class Meta:
        """Choose model Flight and it's fields"""

        model = Flight
        fields = (
            'route_name', 'route', 'departure_time', 'arrival_time',
            'amount_of_free_places', 'url', 'bus_registration_number', 'bus'
        )


class BusSerializer(HyperlinkedModelSerializer):
    """Serializer for model Bus"""

    flights = StringRelatedField(many=True, read_only=True)
    driver_name = ReadOnlyField(source='driver.name')
    driver_second_name = ReadOnlyField(source='driver.second_name')

    class Meta:
        """Choose model Bus and it's fields"""

        model = Bus
        fields = (
            'registration_number', 'mark', 'amount_of_places', 'url',
            'driver_name', 'driver_second_name', 'driver', 'flights'
        )


class DriverSerializer(HyperlinkedModelSerializer):
    """Serializer for model Driver"""

    class Meta:
        """Choose model Driver and it's fields"""

        model = Driver
        fields = (
            'second_name', 'name', 'middle_name',
            'passport_number', 'phone_number', 'age',
        )


class TicketSerializer(HyperlinkedModelSerializer):
    """Serializer for model Ticket"""

    class Meta:
        """Choose model Ticket and it's fields"""

        model = Ticket
        fields = (
            'flight', 'user', 'seller', 'registration_time'
        )
