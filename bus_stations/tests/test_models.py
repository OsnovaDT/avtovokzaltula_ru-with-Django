"""Test models for bus_stations folder"""

from django.test import TestCase

from bus_stations.models import BusStation


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

    def test_max_length(self):
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

    def test_bus_station_model_verbose_name(self):
        """Test verbose_name of BusStation model"""

        bus_station_model_verbose_name = BusStation._meta.verbose_name.title()

        self.assertEqual(
            bus_station_model_verbose_name,
            self.bus_station_model_verbose_name
        )

    def test_bus_station_model_verbose_name_plural(self):
        """Test verbose_name_plural of BusStation model"""

        bus_station_model_verbose_name_plural = \
            BusStation._meta.verbose_name_plural.title()

        self.assertEqual(
            bus_station_model_verbose_name_plural,
            self.bus_station_model_verbose_name_plural
        )

    def test_bus_station_model_ordering(self):
        """Test ordering of BusStation model"""

        bus_station_model_ordering = BusStation._meta.ordering

        self.assertEqual(
            bus_station_model_ordering,
            self.bus_station_model_ordering
        )
