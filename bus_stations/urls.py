from django.urls import path

from .views import Index, RoutesListView, FlightListView

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

    path(
        '<route_id>/flights/',
        FlightListView.as_view(),
        name='flights'
    )
]
