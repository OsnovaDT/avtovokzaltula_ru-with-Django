"""Test models for bus_stations folder"""

from django.test import TestCase
from django.core.validators import MinValueValidator

from bus_stations.models import (
    BusStation, Route, Flight, Bus,
    Driver, Ticket
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

        self.model_verbose_name = 'Автовокзал'
        self.model_verbose_name_plural = 'Автовокзалы'
        self.model_ordering = ['name']

    def test_verbose_names(self):
        """Test verbose_name parameter for fields of BusStation instances"""

        for bus_station in BusStation.objects.all():
            for field, expected_verbose_name in self.fields_and_verbose_names.items():
                real_verbose_name = bus_station._meta.get_field(field).verbose_name

                self.assertEqual(real_verbose_name, expected_verbose_name)

    def test_max_lengths(self):
        """Test max_length parameter for fields of BusStation instances"""

        for bus_station in BusStation.objects.all():
            for field, expected_max_length in self.fields_and_max_lengths.items():
                real_max_length = bus_station._meta.get_field(field).max_length

                self.assertEqual(real_max_length, expected_max_length)

    def test_unique_fields(self):
        """Test BusStation instances for uniqueness"""

        for bus_station in BusStation.objects.all():
            for field in self.unique_fields:
                is_field_unique = bus_station._meta.get_field(field).unique

                self.assertTrue(is_field_unique)

    def test_help_texts(self):
        """Test help_text parameter for fields of BusStation instances"""

        for bus_station in BusStation.objects.all():
            for field, expected_help_text in self.fields_and_help_texts.items():
                real_help_text = bus_station._meta.get_field(field).help_text

                self.assertEqual(real_help_text, expected_help_text)

    def test_instance_string_display(self):
        """Test string display of BusStation instance"""

        for bus_station in BusStation.objects.all():
            instance_string_display = str(bus_station)

            self.assertEqual(instance_string_display, bus_station.name)

    def test_model_verbose_name(self):
        """Test verbose_name of BusStation model"""

        real_model_verbose_name = BusStation._meta.verbose_name.title()

        self.assertEqual(real_model_verbose_name, self.model_verbose_name)

    def test_model_verbose_name_plural(self):
        """Test verbose_name_plural of BusStation model"""

        real_model_verbose_name_plural = \
            BusStation._meta.verbose_name_plural.title()

        self.assertEqual(
            real_model_verbose_name_plural,
            self.model_verbose_name_plural
        )

    def test_model_ordering(self):
        """Test ordering of BusStation model"""

        real_model_ordering = BusStation._meta.ordering

        self.assertEqual(real_model_ordering, self.model_ordering)


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


class FlightTests(TestCase):
    """Test class for Flight model"""

    def setUp(self):
        test_bus_station = BusStation.objects.create(
            name='Автовокзал №1',
            office_hours='10:00 - 22:00',
            address=f'г. Тула, ул. Такая-то, дом №1',
            phone_number=f'8-666-666-69-69'
        )

        test_driver = Driver.objects.create(
            passport_number='1234 12345678',
            name='Семён',
            second_name='Семёнов',
            middle_name='Семёнович',
            phone_number=89206666996,
            age=50
        )

        test_bus = Bus.objects.create(
            registration_number='Е666КХ',
            mark='Ford',
            amount_of_places='40',
            driver=test_driver
        )

        for test_instance_index in range(TEST_INSTANCES_AMOUNT):
            Route.objects.create(
                id=test_instance_index,
                name=f'Маршрут №1',
                regularity='Пн;Ср',
                departure_time='10:00; 22:00',
                price=300,
                bus_station=test_bus_station
            )
            Flight.objects.create(
                route=Route.objects.get(id=test_instance_index),
                departure_time='10:00',
                arrival_time='22:00',
                amount_of_free_places=30,
                bus=test_bus
            )

        # Correct data for Flight model

        self.fields_and_verbose_names = {
            'route': 'Маршрут',
            'departure_time': 'Время отправления',
            'arrival_time': 'Время прибытия',
            'amount_of_free_places': 'Число свободных мест',
            'bus': 'Автобус'
        }

        self.fields_and_default_values = {
            'amount_of_free_places': 30,
        }

        self.model_verbose_name = 'Рейс'
        self.model_verbose_name_plural = 'Рейсы'
        self.model_ordering = ['departure_time']
        self.unique_together = ['route', 'departure_time']

    def test_verbose_names(self):
        """Test verbose_name parameter for fields of Flight instances"""

        for flight in Flight.objects.all():
            for field, expected_verbose_name in self.fields_and_verbose_names.items():
                real_verbose_name = flight._meta.get_field(field).verbose_name

                self.assertEqual(real_verbose_name, expected_verbose_name)

    def test_default_values(self):
        """Test default parameter for fields of Flight instances"""

        for flight in Flight.objects.all():
            for field, expected_default_value in self.fields_and_default_values.items():
                real_default_value = flight._meta.get_field(field).default

                self.assertEqual(real_default_value, expected_default_value)

    def test_instance_string_display(self):
        """Test string display of Flight instance"""

        for flight in Flight.objects.all():
            real_string_display = str(flight)
            expected_string_display = str(flight.route) + ' - ' \
                + str(flight.departure_time)

            self.assertEqual(real_string_display, expected_string_display)

    def test_model_verbose_name(self):
        """Test verbose_name of Flight model"""

        real_model_verbose_name = Flight._meta.verbose_name.title()

        self.assertEqual(real_model_verbose_name, self.model_verbose_name)

    def test_model_verbose_name_plural(self):
        """Test verbose_name_plural of Flight model"""

        real_model_verbose_name_plural = \
            Flight._meta.verbose_name_plural.title()

        self.assertEqual(
            real_model_verbose_name_plural,
            self.model_verbose_name_plural
        )

    def test_model_ordering(self):
        """Test ordering of Flight model"""

        real_model_ordering = Flight._meta.ordering

        self.assertEqual(
            real_model_ordering,
            self.model_ordering
        )


class BusTests(TestCase):
    """Test class for Bus model"""

    def setUp(self):
        for test_instance_index in range(TEST_INSTANCES_AMOUNT):
            test_driver = Driver.objects.create(
                passport_number=f'1234 {test_instance_index}',
                name='Семён',
                second_name='Семёнов',
                middle_name='Семёнович',
                phone_number=test_instance_index,
                age=50
            )
            Bus.objects.create(
                registration_number=f'Е{test_instance_index}КХ',
                mark='Ford',
                amount_of_places='40',
                driver=test_driver
            )

        # Correct data for Bus model

        self.fields_and_verbose_names = {
            'registration_number': 'Регистрационный номер',
            'mark': 'Марка',
            'amount_of_places': 'Число мест',
            'driver': 'Водитель',
        }

        self.fields_and_max_lengths = {
            'registration_number': 10,
            'mark': 100,
        }

        self.primary_key_field = 'registration_number'

        self.model_verbose_name = 'Автобус'
        self.model_verbose_name_plural = 'Автобусы'
        self.model_ordering = ['mark']

    def test_verbose_names(self):
        """Test verbose_name parameter for fields of Bus instances"""

        for bus in Bus.objects.all():
            for field, expected_verbose_name in self.fields_and_verbose_names.items():
                real_verbose_name = bus._meta.get_field(field).verbose_name

                self.assertEqual(real_verbose_name, expected_verbose_name)

    def test_max_lengths(self):
        """Test max_length parameter for fields of BUs instances"""

        for bus in Bus.objects.all():
            for field, expected_max_length in self.fields_and_max_lengths.items():
                real_max_length = bus._meta.get_field(field).max_length

                self.assertEqual(real_max_length, expected_max_length)

    def test_instance_string_display(self):
        """Test string display of Bus instance"""

        for bus in Bus.objects.all():
            real_string_display = str(bus)
            expected_string_display = f'{bus.mark} {bus.registration_number}'

            self.assertEqual(
                real_string_display,
                expected_string_display
            )

    def test_model_verbose_name(self):
        """Test verbose_name of Bus model"""

        real_model_verbose_name = Bus._meta.verbose_name.title()

        self.assertEqual(
            real_model_verbose_name,
            self.model_verbose_name
        )

    def test_model_verbose_name_plural(self):
        """Test verbose_name_plural of Bus model"""

        real_model_verbose_name_plural = \
            Bus._meta.verbose_name_plural.title()

        self.assertEqual(
            real_model_verbose_name_plural,
            self.model_verbose_name_plural
        )

    def test_model_ordering(self):
        """Test ordering of Bus model"""

        real_model_ordering = Bus._meta.ordering

        self.assertEqual(
            real_model_ordering,
            self.model_ordering
        )


class DriverTests(TestCase):
    """Test class for Driver model"""

    def setUp(self):
        for test_instance_index in range(TEST_INSTANCES_AMOUNT):
            Driver.objects.create(
                passport_number=test_instance_index,
                name='Евгений',
                second_name='Иванов',
                middle_name='Иванович',
                phone_number=test_instance_index,
                age=30
            )

        # Correct data for Driver model

        self.fields_and_verbose_names = {
            'passport_number': 'Номер паспорта',
            'name': 'Имя',
            'second_name': 'Фамилия',
            'middle_name': 'Отчество',
            'phone_number': 'Номер телефона',
            'age': 'Возраст',
        }

        self.fields_and_max_lengths = {
            'passport_number': 25,
            'name': 255,
            'second_name': 255,
            'middle_name': 255,
        }

        self.fields_and_validators = {
            'phone_number': [MinValueValidator(1)],
            'age': [MinValueValidator(21)],
        }

        self.unique_fields = ['passport_number', 'phone_number']

        self.model_verbose_name = 'Водитель'
        self.model_verbose_name_plural = 'Водители'
        self.model_ordering = ['name', 'second_name', 'middle_name']

    def test_verbose_names(self):
        """Test verbose_name parameter for fields of Driver instances"""

        for driver in Driver.objects.all():
            for field, expected_verbose_name in self.fields_and_verbose_names.items():
                real_verbose_name = driver._meta.get_field(field).verbose_name

                self.assertEqual(real_verbose_name, expected_verbose_name)

    def test_max_lengths(self):
        """Test max_length parameter for fields of Driver instances"""

        for driver in Driver.objects.all():
            for field, expected_max_length in self.fields_and_max_lengths.items():
                real_max_length = driver._meta.get_field(field).max_length

                self.assertEqual(real_max_length, expected_max_length)

    def test_unique_fields(self):
        """Test Driver instances for uniqueness"""

        for driver in Driver.objects.all():
            for field in self.unique_fields:
                is_field_unique = driver._meta.get_field(field).unique

                self.assertTrue(is_field_unique)

    def test_validators(self):
        """Test validators parameter for fields of Driver instances"""

        for driver in Driver.objects.all():
            for field, expected_validators in self.fields_and_validators.items():
                real_validators = driver._meta.get_field(field).validators

                self.assertEqual(real_validators, expected_validators)

    def test_instance_string_display(self):
        """Test string display of Driver instance"""

        for driver in Driver.objects.all():
            real_string_display = str(driver)
            expected_string_display = str(driver.second_name) + " " + \
                str(driver.name[0]) + "." + \
                str(driver.middle_name[0]) + ". - " + \
                str(driver.passport_number)

            self.assertEqual(
                real_string_display,
                expected_string_display
            )

    def test_model_verbose_name(self):
        """Test verbose_name of Driver model"""

        real_model_verbose_name = Driver._meta.verbose_name.title()

        self.assertEqual(real_model_verbose_name, self.model_verbose_name)

    def test_model_verbose_name_plural(self):
        """Test verbose_name_plural of Driver model"""

        real_model_verbose_name_plural = \
            Driver._meta.verbose_name_plural.title()

        self.assertEqual(
            real_model_verbose_name_plural,
            self.model_verbose_name_plural
        )

    def test_model_ordering(self):
        """Test ordering of Driver model"""

        real_model_ordering = Driver._meta.ordering

        self.assertEqual(real_model_ordering, self.model_ordering)
