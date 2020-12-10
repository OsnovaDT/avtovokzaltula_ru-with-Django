from django.urls import path

from .views import (
    Index, RoutesListView, FlightListView,
    SellTicketView, TicketListView,
    DeleteTicketView, ChequeForTicketView
)

app_name = 'bus_stations'

urlpatterns = [
    # Index
    path('', Index.as_view(), name='index'),

    # Bus station's routes
    path(
        '<bus_station_id>/routes/',
        RoutesListView.as_view(),
        name='routes'
    ),

    # Route's flights
    path(
        '<route_id>/flights/',
        FlightListView.as_view(),
        name='flights'
    ),

    # Sell ticket
    path(
        'sell_ticket/',
        SellTicketView.as_view(),
        name='sell_ticket'
    ),

    # Print all tickets
    path(
        'flight/<int:flight_id>/tickets/',
        TicketListView.as_view(),
        name='tickets',
    ),

    # Delete ticket
    path(
        'delete_ticket/<int:pk>/',
        DeleteTicketView.as_view(),
        name='delete_ticket'
    ),

    # Cheque for ticket
    path(
        'cheque_for_ticket/',
        ChequeForTicketView.as_view(),
        name='cheque_for_ticket'
    ),
]
