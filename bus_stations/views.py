from time import gmtime

from .models import (
    BusStation, Route, Flight,
    Bus, Driver, Ticket
)
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import (
    LoginRequiredMixin, UserPassesTestMixin
)
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView
from django.forms import ValidationError

from .forms import SellTicketForm


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
        ).select_related('route', 'bus', 'route__bus_station')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['route'] = Route.objects.get(
            pk=self.kwargs['route_id']
        )

        # Next flight
        context['next_flight'] = get_next_flight(
            Flight.objects.filter(
                route=context['route']
            )
        )

        context['tickets'] = Ticket.objects.filter(
            flight__route=context['route']
        )

        context['travel_time'] = get_travel_time(
            Flight.objects.filter(
                route=self.kwargs['route_id']
            ).first().departure_time,
            Flight.objects.filter(
                route=self.kwargs['route_id']
            ).first().arrival_time
        )

        return context


class SellTicketView(UserPassesTestMixin, CreateView):
    form_class = SellTicketForm
    template_name = 'bus_stations/sell_ticket.html'
    success_url = reverse_lazy('bus_stations:cheque_for_ticket')

    def form_valid(self, SellTicketForm):
        sell_ticket_flight = Flight.objects.get(
            pk=self.get_form_kwargs()['data']['flight']
        )

        sell_ticket_flight.amount_of_free_places -= 1
        sell_ticket_flight.save()

        return super().form_valid(SellTicketForm)

    def test_func(self):
        return self.request.user.is_staff


class ChequeForTicketView(TemplateView):
    template_name = 'bus_stations/cheque_for_ticket.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['ticket'] = Ticket.objects.latest()

        return context


class TicketListView(UserPassesTestMixin, ListView):
    template_name = 'bus_stations/tickets.html'
    context_object_name = 'tickets'

    def test_func(self):
        return self.request.user.is_staff

    def get_queryset(self):
        return Ticket.objects.filter(
            flight=self.kwargs['flight_id'],
        )

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['flight'] = Flight.objects.get(
            pk=self.kwargs['flight_id']
        )

        return context


class DeleteTicketView(UserPassesTestMixin, DeleteView):
    template_name = 'bus_stations/delete_ticket.html'
    model = Ticket
    success_url = reverse_lazy('bus_stations:index')

    def test_func(self):
        return self.request.user.is_staff

    def get_success_url(self):
        delete_ticket_flight = Flight.objects.get(
            pk=Ticket.objects.get(pk=self.kwargs['pk']).flight.pk
        )
        delete_ticket_flight.amount_of_free_places += 1
        delete_ticket_flight.save()

        return reverse_lazy(
            'bus_stations:tickets',
            args=[delete_ticket_flight.pk]
        )

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context[
            'flight'
        ] = Flight.objects.get(
            pk=Ticket.objects.get(pk=self.kwargs['pk']).flight.pk
        )
        return context


def get_travel_time(departure_time, arrival_time):
    departure_hours_in_minute = int(str(departure_time)[:2]) * 60
    arrival_hours_in_minute = int(str(arrival_time)[:2]) * 60

    departure_minute = int(str(departure_time)[3:5])
    arrival_minute = int(str(arrival_time)[3:5])

    travel_minute = (arrival_hours_in_minute + arrival_minute) - \
        (departure_hours_in_minute + departure_minute)

    return f'{travel_minute // 60}:{travel_minute % 60}:00'


def get_next_flight(flights):
    current_hour = gmtime()[3] + 3
    current_minute = gmtime()[4]

    # Flights with departure hour more than current hour
    flights_after_current_hour = []
    for flight in flights:
        # If flight's departure hour more or equal than current hour
        if int(str(flight.departure_time)[:2]) >= current_hour:
            flights_after_current_hour.append(flight)
    if not flights_after_current_hour:
        return ''
    else:
        # Flights with departure time more than current time
        flights_after_current_time = []
        for flight in flights_after_current_hour:
            # If flight's departure minute more or equal than current minute
            if int(str(flight.departure_time)[3:5]) >= current_minute and \
                    int(str(flight.departure_time)[:2]) == current_hour:
                flights_after_current_time.append(flight)

            if int(str(flight.departure_time)[:2]) > current_hour:
                flights_after_current_time.append(flight)

        return get_flight_with_non_zero_free_places_amount(flights_after_current_time)


def get_flight_with_non_zero_free_places_amount(flights):
    for i in range(len(flights)):
        next_flight = flights[i]

        if next_flight.amount_of_free_places != 0:
            break
        else:
            while next_flight.amount_of_free_places == 0:
                i += 1
                if i >= len(flights):
                    next_flight = ''
                    break
                next_flight = flights[i]
                if next_flight.amount_of_free_places != 0:
                    break

    return next_flight
