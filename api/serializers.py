"""Serializers for API"""

from django.contrib.auth.models import User
from rest_framework.serializers import HyperlinkedModelSerializer

from bus_stations.models import BusStation, Route


class UserSerializer(HyperlinkedModelSerializer):
    """Serializer for model User"""

    class Meta:
        """Choose model User and it's fields"""

        model = User
        fields = ('username', 'email', 'url', 'groups')


class BusStationSerializer(HyperlinkedModelSerializer):
    """Serializer for model BusStation"""

    class Meta:
        """Choose model BusStation and it's fields"""

        model = BusStation
        fields = (
            'name', 'office_hours',
            'address', 'phone_number'
        )


class RouteSerializer(HyperlinkedModelSerializer):
    """Serializer for model Route"""

    class Meta:
        """Choose model Route and it's fields"""

        model = Route
        fields = (
            'name', 'regularity', 'departure_time',
            'price', 'bus_station'
        )
