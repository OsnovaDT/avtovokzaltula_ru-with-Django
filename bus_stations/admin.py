from django.contrib import admin


from .models import (
    BusStation, Route, Flight, Bus, Driver, Ticket
)


class BusStationAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'office_hours',
        'address', 'phone_number'
    )
    list_display_links = ('name',)
    search_fields = ('name',)


class RouteAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'regularity',
        'departure_time',
        'price', 'bus_station'
    )
    list_display_links = ('name', 'bus_station')
    search_fields = ('name', 'bus_station')


class FlightAdmin(admin.ModelAdmin):
    list_display = (
        'route', 'departure_time', 'arrival_time',
        'amount_of_free_places', 'bus'
    )
    list_display_links = ('route', 'bus')
    search_fields = ('route', 'bus')


class BusAdmin(admin.ModelAdmin):
    list_display = (
        'registration_number', 'mark',
        'amount_of_places'
    )
    list_display_links = ('mark',)
    search_fields = ('mark', 'registration_number')


class DriverAdmin(admin.ModelAdmin):
    list_display = (
        'passport_number', 'name',
        'second_name', 'middle_name',
        'phone_number', 'age', 'bus'
    )
    list_display_links = ('name', 'bus')
    search_fields = ('name', 'bus', 'passport_number')


class TicketAdmin(admin.ModelAdmin):
    list_display = (
        'bus_station', 'route',
        'price', 'user',
        'seller'
    )
    list_display_links = ('bus_station', 'route', 'user', 'seller')
    search_fields = ('bus_station', 'route', 'user', 'seller')


admin.site.register(BusStation, BusStationAdmin)
admin.site.register(Route, RouteAdmin)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Bus, BusAdmin)
admin.site.register(Driver, DriverAdmin)
admin.site.register(Ticket, TicketAdmin)
