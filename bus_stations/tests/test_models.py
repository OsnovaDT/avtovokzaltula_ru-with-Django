"""Test models for bus_stations folder"""

from datetime import time

from django.test import TestCase
from django.core.validators import MinValueValidator

from bus_stations.models import (
    BusStation, Route, Flight,
    Bus, Driver, Ticket
)


TEST_INSTANCES_AMOUNT = 20

# Mixins


class TestVerboseNamesMixin():
    """Mixin with function for testing verbose_names"""

    def test_verbose_names(self, model):
        """Test verbose_name parameter for fields of model instances"""

        for instance in model.objects.all():
            for field, expected_verbose_name in self.fields_and_verbose_names.items():
                real_verbose_name = instance._meta.get_field(field).verbose_name

                self.assertEqual(real_verbose_name, expected_verbose_name)


class TestMaxLengthsMixin():
    """Mixin with function for testing max_lengths"""

    def test_max_lengths(self, model):
        """Test max_length parameter for fields of model instances"""

        for instance in model.objects.all():
            for field, expected_max_length in self.fields_and_max_lengths.items():
                real_max_length = instance._meta.get_field(field).max_length

                self.assertEqual(real_max_length, expected_max_length)


class TestHelpTextsMixin():
    """Mixin with function for testing help_texts"""

    def test_help_texts(self, model):
        """Test help_text parameter for fields of model instances"""

        for instance in model.objects.all():
            for field, expected_help_text in self.fields_and_help_texts.items():
                real_help_text = instance._meta.get_field(field).help_text

                self.assertEqual(real_help_text, expected_help_text)


class TestVerboseNameOfModelMixin():
    """Mixin with function for testing verbose_name of model"""

    def test_verbose_name_of_model(self, model):
        """Test verbose_name of the model"""

        real_model_verbose_name = model._meta.verbose_name.title()
        expected_model_verbose_name = self.model_verbose_name

        self.assertEqual(real_model_verbose_name, expected_model_verbose_name)


class TestVerboseNamePluralOfModelMixin():
    """Mixin with function for testing verbose_name_plural of model"""

    def test_verbose_name_plural_of_model(self, model):
        """Test verbose_name_plural of the model"""

        real_model_verbose_name_plural = \
            model._meta.verbose_name_plural.title()

        expected_model_verbose_name_plural = self.model_verbose_name_plural

        self.assertEqual(
            real_model_verbose_name_plural,
            expected_model_verbose_name_plural
        )


class TestOrderingOfModelMixin():
    """Mixin with function for testing ordering of model"""

    def test_ordering_of_model(self, model):
        """Test ordering of the model"""

        real_model_ordering = model._meta.ordering
        expected_model_ordering = self.model_ordering

        self.assertEqual(real_model_ordering, expected_model_ordering)


class TestInstanceStringDisplayMixin():
    """Mixin with function for testing instance string display"""

    def test_instance_string_display(self, instance, expected_string_display):
        """Test string display of the model instance"""

        real_string_display = str(instance)

        self.assertEqual(real_string_display, expected_string_display)


class TestUniqueFieldsMixin():
    """Mixin with function for testing unique fields"""

    def test_unique_fields(self, model):
        """Test model instances for uniqueness"""

        for instance in model.objects.all():
            for field in self.unique_fields:
                is_field_unique = instance._meta.get_field(field).unique

                self.assertTrue(is_field_unique)


class TestValidatorsMixin():
    """Mixin with function for testing validators"""

    def test_validators(self, model):
        """Test validators parameter for fields of model instances"""

        for instance in model.objects.all():
            for field, expected_validators in self.fields_and_validators.items():
                real_validators = instance._meta.get_field(field).validators

                self.assertEqual(real_validators, expected_validators)


class TestDefaultValuesMixin():
    """Mixin with function for testing default values"""

    def test_default_values(self, model):
        """Test default parameter for fields of the model"""

        for instance in model.objects.all():
            for field, expected_default_value in self.fields_and_default_values.items():
                real_default_value = instance._meta.get_field(field).default

                self.assertEqual(real_default_value, expected_default_value)


class TestGetLatestByOfModelMixin():
    """Mixin with function for testing get_latest_by of model"""

    def test_get_latest_by_of_model(self, model):
        """Test get_latest_by of the model"""

        real_model_get_latest_by = model._meta.get_latest_by

        self.assertEqual(real_model_get_latest_by, self.model_get_latest_by)


# Test classes


class BusStationTests(
        TestCase, TestVerboseNamesMixin, TestMaxLengthsMixin,
        TestHelpTextsMixin, TestVerboseNameOfModelMixin,
        TestVerboseNamePluralOfModelMixin, TestOrderingOfModelMixin,
        TestInstanceStringDisplayMixin, TestUniqueFieldsMixin
    ):
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

        self.fields_and_help_texts = {
            'office_hours': 'Часы работы через точку с запятой',
        }

        self.unique_fields = ['name', 'address', 'phone_number']

        self.model_verbose_name = 'Автовокзал'
        self.model_verbose_name_plural = 'Автовокзалы'
        self.model_ordering = ['name']

    def test_verbose_names(self):
        """Test verbose_name parameter for fields of BusStation instances"""

        super().test_verbose_names(BusStation)

    def test_max_lengths(self):
        """Test max_length parameter for fields of BusStation instances"""

        super().test_max_lengths(BusStation)

    def test_help_texts(self):
        """Test help_text parameter for fields of BusStation instances"""

        super().test_help_texts(BusStation)

    def test_unique_fields(self):
        """Test BusStation instances for uniqueness"""

        super().test_unique_fields(BusStation)

    def test_instance_string_display(self):
        """Test string display of BusStation instance"""

        for bus_station in BusStation.objects.all():
            expected_string_display = bus_station.name

            super().test_instance_string_display(
                bus_station, expected_string_display
            )

    def test_verbose_name_of_model(self):
        """Test verbose_name of BusStation model"""

        super().test_verbose_name_of_model(BusStation)

    def test_verbose_name_plural_of_model(self):
        """Test verbose_name_plural of BusStation model"""

        super().test_verbose_name_plural_of_model(BusStation)

    def test_ordering_of_model(self):
        """Test ordering of BusStation model"""

        super().test_ordering_of_model(BusStation)


class RouteTests(
        TestCase, TestVerboseNamesMixin, TestInstanceStringDisplayMixin,
        TestHelpTextsMixin, TestVerboseNameOfModelMixin, TestMaxLengthsMixin,
        TestVerboseNamePluralOfModelMixin, TestOrderingOfModelMixin,
    ):
    """Test class for Route model"""

    def setUp(self):
        test_bus_station = BusStation.objects.create(
            name='Автовокзал №1',
            office_hours='10:00 - 22:00',
            address='г. Тула, ул. Такая-то, дом №1',
            phone_number='8-666-666-69-69'
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

        super().test_verbose_names(Route)

    def test_max_lengths(self):
        """Test max_length parameter for fields of Route instances"""

        super().test_max_lengths(Route)

    def test_help_texts(self):
        """Test help_text parameter for fields of Route instances"""

        super().test_help_texts(Route)

    def test_instance_string_display(self):
        """Test string display of Route instance"""

        for route in Route.objects.all():
            expected_string_display = str(route.bus_station) + ' - ' \
                + str(route.name)

            super().test_instance_string_display(
                route, expected_string_display
            )

    def test_verbose_name_of_model(self):
        """Test verbose_name of Route model"""

        super().test_verbose_name_of_model(Route)

    def test_verbose_name_plural_of_model(self):
        """Test verbose_name_plural of Route model"""

        super().test_verbose_name_plural_of_model(Route)

    def test_ordering_of_model(self):
        """Test ordering of Route model"""

        super().test_ordering_of_model(Route)


class FlightTests(
        TestCase, TestVerboseNamesMixin, TestVerboseNameOfModelMixin,
        TestVerboseNamePluralOfModelMixin, TestOrderingOfModelMixin,
        TestInstanceStringDisplayMixin, TestDefaultValuesMixin
    ):
    """Test class for Flight model"""

    def setUp(self):
        test_bus_station = BusStation.objects.create(
            name='Автовокзал №1',
            office_hours='10:00 - 22:00',
            address='г. Тула, ул. Такая-то, дом №1',
            phone_number='8-666-666-69-69'
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
                name='Маршрут №1',
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

        super().test_verbose_names(Flight)

    def test_default_values(self):
        """Test default parameter for fields of Flight instances"""

        super().test_default_values(Flight)

    def test_instance_string_display(self):
        """Test string display of Flight instance"""

        for flight in Flight.objects.all():
            expected_string_display = str(flight.route) + ' - ' \
                + str(flight.departure_time)

            super().test_instance_string_display(
                flight, expected_string_display
            )

    def test_verbose_name_of_model(self):
        """Test verbose_name of Flight model"""

        super().test_verbose_name_of_model(Flight)

    def test_verbose_name_plural_of_model(self):
        """Test verbose_name_plural of Flight model"""

        super().test_verbose_name_plural_of_model(Flight)

    def test_ordering_of_model(self):
        """Test ordering of Flight model"""

        super().test_ordering_of_model(Flight)


class BusTests(
        TestCase, TestVerboseNamesMixin, TestMaxLengthsMixin,
        TestVerboseNameOfModelMixin, TestVerboseNamePluralOfModelMixin,
        TestOrderingOfModelMixin, TestInstanceStringDisplayMixin
    ):
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

        super().test_verbose_names(Bus)

    def test_max_lengths(self):
        """Test max_length parameter for fields of Bus instances"""

        super().test_max_lengths(Bus)

    def test_instance_string_display(self):
        """Test string display of Bus instance"""

        for bus in Bus.objects.all():
            expected_string_display = f'{bus.mark} {bus.registration_number}'

            super().test_instance_string_display(
                bus, expected_string_display
            )

    def test_verbose_name_of_model(self):
        """Test verbose_name of Bus model"""

        super().test_verbose_name_of_model(Bus)

    def test_verbose_name_plural_of_model(self):
        """Test verbose_name_plural of Bus model"""

        super().test_verbose_name_plural_of_model(Bus)

    def test_ordering_of_model(self):
        """Test ordering of Bus model"""

        super().test_ordering_of_model(Bus)


class DriverTests(
        TestCase, TestVerboseNamesMixin, TestMaxLengthsMixin,
        TestVerboseNameOfModelMixin, TestVerboseNamePluralOfModelMixin,
        TestOrderingOfModelMixin, TestInstanceStringDisplayMixin,
        TestUniqueFieldsMixin, TestValidatorsMixin
    ):
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

        super().test_verbose_names(Driver)

    def test_max_lengths(self):
        """Test max_length parameter for fields of Driver instances"""

        super().test_max_lengths(Driver)

    def test_unique_fields(self):
        """Test Driver instances for uniqueness"""

        super().test_unique_fields(Driver)

    def test_validators(self):
        """Test validators parameter for fields of Driver instances"""

        super().test_validators(Driver)

    def test_instance_string_display(self):
        """Test string display of Driver instance"""

        for driver in Driver.objects.all():
            expected_string_display = str(driver.second_name) + " " \
                + str(driver.name[0]) + "." + str(driver.middle_name[0]) \
                + ". - " + str(driver.passport_number)

            super().test_instance_string_display(
                driver, expected_string_display
            )

    def test_verbose_name_of_model(self):
        """Test verbose_name of Driver model"""

        super().test_verbose_name_of_model(Driver)

    def test_verbose_name_plural_of_model(self):
        """Test verbose_name_plural of Driver model"""

        super().test_verbose_name_plural_of_model(Driver)

    def test_ordering_of_model(self):
        """Test ordering of Driver model"""

        super().test_ordering_of_model(Driver)


class TicketTests(
        TestCase, TestVerboseNamesMixin, TestMaxLengthsMixin,
        TestVerboseNameOfModelMixin, TestVerboseNamePluralOfModelMixin,
        TestOrderingOfModelMixin, TestInstanceStringDisplayMixin,
        TestGetLatestByOfModelMixin
    ):
    """Test class for Ticket model"""

    def setUp(self):
        for test_instance_index in range(TEST_INSTANCES_AMOUNT):
            test_bus_station = BusStation.objects.create(
                name=f'Автовокзал №{test_instance_index}',
                office_hours='10:00 - 22:00',
                address=f'г. Тула, ул. Такая-то, дом №{test_instance_index}',
                phone_number=f'8-666-666-69-{test_instance_index}'
            )

            test_route = Route.objects.create(
                name=f'Маршрут №{test_instance_index}',
                regularity='Пн;Ср',
                departure_time='10:00; 22:00',
                price=300,
                bus_station=test_bus_station
            )

            test_driver = Driver.objects.create(
                passport_number=test_instance_index,
                name='Евгений',
                second_name='Иванов',
                middle_name='Иванович',
                phone_number=test_instance_index,
                age=30
            )

            test_bus = Bus.objects.create(
                registration_number=f'Е{test_instance_index}КХ',
                mark='Ford',
                amount_of_places='40',
                driver=test_driver
            )

            test_flight = Flight.objects.create(
                route=test_route,
                departure_time='10:00',
                arrival_time='22:00',
                amount_of_free_places=30,
                bus=test_bus
            )

            Ticket.objects.create(
                flight=test_flight,
                user='Евгений',
                seller='Иван',
                registration_time=time(12, 30),
            )

        # Correct data for Driver model

        self.fields_and_verbose_names = {
            'flight': 'Рейс',
            'user': 'Покупатель',
            'seller': 'Продавец',
            'registration_time': 'Время оформления',
        }

        self.fields_and_max_lengths = {
            'user': 255,
            'seller': 255,
        }

        self.model_verbose_name = 'Билет'
        self.model_verbose_name_plural = 'Билеты'
        self.model_ordering = ['flight']
        self.model_get_latest_by = 'registration_time'

    def test_verbose_names(self):
        """Test verbose_name parameter for fields of Ticket instances"""

        super().test_verbose_names(Ticket)

    def test_max_lengths(self):
        """Test max_length parameter for fields of Ticket instances"""

        super().test_max_lengths(Ticket)

    def test_instance_string_display(self):
        """Test string display of Ticket instance"""

        for ticket in Ticket.objects.all():
            expected_string_display = str(ticket.flight) + " - " \
                + str(ticket.user)
            super().test_instance_string_display(
                ticket, expected_string_display
            )

    def test_verbose_name_of_model(self):
        """Test verbose_name of Ticket model"""

        super().test_verbose_name_of_model(Ticket)

    def test_verbose_name_plural_of_model(self):
        """Test verbose_name_plural of Ticket model"""

        super().test_verbose_name_plural_of_model(Ticket)

    def test_ordering_of_model(self):
        """Test ordering of Ticket model"""

        super().test_ordering_of_model(Ticket)

    def test_get_latest_by_of_model(self):
        """Test get_latest_by of Ticket model"""

        super().test_get_latest_by_of_model(Ticket)
