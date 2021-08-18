"""Serializers for API"""

from django.contrib.auth.models import User
from rest_framework.serializers import (
    HyperlinkedModelSerializer, StringRelatedField,
    ReadOnlyField
)

from bus_stations.models import BusStation, Route


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

    class Meta:
        """Choose model Route and it's fields"""

        model = Route
        fields = (
            'name', 'regularity', 'departure_time',
            'price', 'bus_station_name', 'bus_station', 'url'
        )
