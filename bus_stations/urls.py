from django.urls import path

from .views import (
    Index, RoutesListView, FlightListView,
    SellTicketView
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

    # Path to buy ticket form
    path(
        'buy_ticket',
        SellTicketView.as_view(),
        name='buy_ticket'
    )
]
