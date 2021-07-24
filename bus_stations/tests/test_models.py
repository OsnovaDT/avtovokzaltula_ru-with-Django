"""Test models for bus_stations folder"""

from django.test import TestCase

from bus_stations.models import (
    BusStation, Route,
)


TEST_INSTANCES_AMOUNT = 20


class BusStationTests(TestCase):
    """Test class for BusStation model"""

    def setUp(self):
        for test_instance_index in range(TEST_INSTANCES_AMOUNT):
            BusStation.objects.create(
                name=f'Автовокзал №{test_instance_index}',
                office_hours='10:00 - 22:00',
                address=f'г. Тула, ул. Такая-то, дом №{test_instance_index}',
                phone_number=f'8-666-666-69-{test_instance_index}'
            )

        # Correct data for BusStation model

        self.fields_and_verbose_names = {
            'name': 'Название',
            'office_hours': 'Часы работы',
            'address': 'Адрес',
            'phone_number': 'Номер телефона',
        }

        self.fields_and_max_lengths = {
            'name': 50,
            'office_hours': 30,
            'address': 100,
            'phone_number': 15,
        }

        self.unique_fields = ['name', 'address', 'phone_number']

        self.fields_and_help_texts = {
            'office_hours': 'Часы работы через точку с запятой',
        }

        self.bus_station_model_verbose_name = 'Автовокзал'
        self.bus_station_model_verbose_name_plural = 'Автовокзалы'
        self.bus_station_model_ordering = ['name']

    def test_verbose_names(self):
        """Test verbose_name parameter for fields of BusStation instances"""

        for bus_station in BusStation.objects.all():
            for field, correct_verbose_name in self.fields_and_verbose_names.items():
                field_verbose_name = bus_station._meta.get_field(field).verbose_name

                self.assertEqual(field_verbose_name, correct_verbose_name)

    def test_max_lengths(self):
        """Test max_length parameter for fields of BusStation instances"""

        for bus_station in BusStation.objects.all():
            for field, correct_max_length in self.fields_and_max_lengths.items():
                field_max_length = bus_station._meta.get_field(field).max_length

                self.assertEqual(field_max_length, correct_max_length)

    def test_unique_fields(self):
        """Test BusStation instances for uniqueness"""

        for bus_station in BusStation.objects.all():
            for field in self.unique_fields:
                is_field_unique = bus_station._meta.get_field(field).unique

                self.assertTrue(is_field_unique)

    def test_help_texts(self):
        """Test help_text parameter for fields of BusStation instances"""

        for bus_station in BusStation.objects.all():
            for field, correct_help_text in self.fields_and_help_texts.items():
                field_help_text = bus_station._meta.get_field(field).help_text

                self.assertEqual(field_help_text, correct_help_text)

    def test_instance_string_display(self):
        """Test string display of BusStation instance"""

        for bus_station in BusStation.objects.all():
            bus_station_string_display = str(bus_station)

            self.assertEqual(bus_station_string_display, bus_station.name)

    def test_model_verbose_name(self):
        """Test verbose_name of BusStation model"""

        bus_station_model_verbose_name = BusStation._meta.verbose_name.title()

        self.assertEqual(
            bus_station_model_verbose_name,
            self.bus_station_model_verbose_name
        )

    def test_model_verbose_name_plural(self):
        """Test verbose_name_plural of BusStation model"""

        bus_station_model_verbose_name_plural = \
            BusStation._meta.verbose_name_plural.title()

        self.assertEqual(
            bus_station_model_verbose_name_plural,
            self.bus_station_model_verbose_name_plural
        )

    def test_model_ordering(self):
        """Test ordering of BusStation model"""

        bus_station_model_ordering = BusStation._meta.ordering

        self.assertEqual(
            bus_station_model_ordering,
            self.bus_station_model_ordering
        )


class RouteTests(TestCase):
    """Test class for Route model"""

    def setUp(self):
        test_bus_station = BusStation.objects.create(
            name='Автовокзал №1',
            office_hours='10:00 - 22:00',
            address=f'г. Тула, ул. Такая-то, дом №1',
            phone_number=f'8-666-666-69-69'
        )

        for test_instance_index in range(TEST_INSTANCES_AMOUNT):
            Route.objects.create(
                name=f'Маршрут №{test_instance_index}',
                regularity='Пн;Ср',
                departure_time='10:00; 22:00',
                price=300,
                bus_station=test_bus_station
            )

        # Correct data for Route model

        self.fields_and_verbose_names = {
            'name': 'Название',
            'regularity': 'Регулярность',
            'departure_time': 'Время отправления',
            'price': 'Цена',
            'bus_station': 'Автовокзал'
        }

        self.fields_and_max_lengths = {
            'name': 100,
            'regularity': 20,
            'departure_time': 255,
        }

        self.fields_and_help_texts = {
            'name': 'Пункт прибытия',
            'regularity': 'Первые 2 буквы дней недели через точку с запятой,\
            либо Еж - ежедневно',
            'departure_time': 'Всё возможное время отправления',
        }

        self.model_verbose_name = 'Маршрут'
        self.model_verbose_name_plural = 'Маршруты'
        self.model_ordering = ['name']

    def test_verbose_names(self):
        """Test verbose_name parameter for fields of Route instances"""

        for route in Route.objects.all():
            for field, expected_verbose_name in self.fields_and_verbose_names.items():
                real_verbose_name = route._meta.get_field(field).verbose_name

                self.assertEqual(real_verbose_name, expected_verbose_name)

    def test_max_lengths(self):
        """Test max_length parameter for fields of Route instances"""

        for route in Route.objects.all():
            for field, expected_max_length in self.fields_and_max_lengths.items():
                real_max_length = route._meta.get_field(field).max_length

                self.assertEqual(real_max_length, expected_max_length)

    def test_help_texts(self):
        """Test help_text parameter for fields of Route instances"""

        for route in Route.objects.all():
            for field, expected_help_text in self.fields_and_help_texts.items():
                real_help_text = route._meta.get_field(field).help_text

                self.assertEqual(real_help_text, expected_help_text)

    def test_instance_string_display(self):
        """Test string display of Route instance"""

        for route in Route.objects.all():
            real_string_display = str(route)
            expected_string_display = str(route.bus_station) + ' - ' \
                + str(route.name)

            self.assertEqual(
                real_string_display,
                expected_string_display
            )

    def test_model_verbose_name(self):
        """Test verbose_name of Route model"""

        real_model_verbose_name = Route._meta.verbose_name.title()

        self.assertEqual(
            real_model_verbose_name,
            self.model_verbose_name
        )

    def test_model_verbose_name_plural(self):
        """Test verbose_name_plural of Route model"""

        real_model_verbose_name_plural = \
            Route._meta.verbose_name_plural.title()

        self.assertEqual(
            real_model_verbose_name_plural,
            self.model_verbose_name_plural
        )

    def test_model_ordering(self):
        """Test ordering of Route model"""

        real_model_ordering = Route._meta.ordering

        self.assertEqual(
            real_model_ordering,
            self.model_ordering
        )
