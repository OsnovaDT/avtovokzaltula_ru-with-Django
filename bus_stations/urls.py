from django.urls import path

from .views import Index

app_name = 'bus_stations'

urlpatterns = [
    path('', Index.as_view(), name='index')
]
