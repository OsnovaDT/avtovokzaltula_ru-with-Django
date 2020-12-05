from django.views.generic.list import ListView

from .models import BusStation, Route, Flight, Bus, Driver


class Index(ListView):
    template_name = 'bus_stations/index.html'
    context_object_name = 'bus_stations'
    queryset = BusStation.objects.all()
