from .models import BusStation, Route, Flight, Bus, Driver
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin


class Index(LoginRequiredMixin, ListView):
    template_name = 'bus_stations/index.html'
    context_object_name = 'bus_stations'
    queryset = BusStation.objects.all()


class RoutesListView(LoginRequiredMixin, ListView):
    template_name = 'bus_stations/bus_station_routes.html'
    context_object_name = 'routes'

    def get_queryset(self):
        return Route.objects.filter(
            bus_station=self.kwargs['bus_station_id']
        )

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['bus_station'] = BusStation.objects.get(
            pk=self.kwargs['bus_station_id']
        )

        return context


class FlightListView(LoginRequiredMixin, ListView):
    template_name = 'bus_stations/route_flights.html'
    context_object_name = 'flights'

    def get_queryset(self):
        return Flight.objects.filter(
            route=self.kwargs['route_id']
        ).select_related('route', 'bus_station', 'bus')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['route'] = Route.objects.select_related(
            'bus_station'
        ).get(pk=self.kwargs['route_id'])

        return context
