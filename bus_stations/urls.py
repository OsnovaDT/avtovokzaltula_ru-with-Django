from django.urls import path

from .views import (
    Index, RoutesListView, FlightListView,
    SellTicketView, TicketListView,
    DeleteTicketView
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

    path(
        'delete_ticket/<int:pk>/',
        DeleteTicketView.as_view(),
        name='delete_ticket'
    )
]
