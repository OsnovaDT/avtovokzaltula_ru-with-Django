from django.db import models
from django.core.validators import MinValueValidator


class BusStation(models.Model):
    name = models.CharField(
        'Название',
        max_length=50,
        unique=True,
    )

    office_hours = models.CharField(
        'Часы работы',
        help_text='Часы работы через точку с запятой',
        max_length=30,
    )

    address = models.CharField(
        'Адрес',
        max_length=100,
        unique=True,
    )

    phone_number = models.CharField(
        'Номер телефона',
        max_length=15,
        unique=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Автовокзал'
        verbose_name_plural = 'Автовокзалы'
        ordering = ['name']


class Route(models.Model):
    name = models.CharField(
        'Название',
        help_text='Пункт прибытия',
        max_length=100,
    )

    regularity = models.CharField(
        'Регулярность',
        help_text='Первые 2 буквы дней недели через точку с запятой,\
            либо Еж - ежедневно',
        max_length=20,
    )

    departure_time = models.CharField(
        'Время отправления',
        help_text='Всё возможное время отправления',
        max_length=255,
    )

    price = models.PositiveSmallIntegerField(
        'Цена',
    )

    bus_station = models.ForeignKey(
        'BusStation',
        on_delete=models.CASCADE,
        verbose_name='Автовокзал',
    )

    def __str__(self):
        return str(self.bus_station) + " - " + str(self.name)

    class Meta:
        verbose_name = 'Маршрут'
        verbose_name_plural = 'Маршруты'
        ordering = ['name']


class Flight(models.Model):
    route = models.ForeignKey(
        'Route',
        on_delete=models.CASCADE,
        verbose_name='Маршрут'
    )

    departure_time = models.TimeField(
        'Время отправления',
    )

    arrival_time = models.TimeField(
        'Время прибытия',
    )

    amount_of_free_places = models.PositiveSmallIntegerField(
        'Число свободных мест',
        default=30,
    )

    bus = models.ForeignKey(
        'Bus',
        on_delete=models.CASCADE,
        verbose_name='Автобус',
    )

    def __str__(self):
        return str(self.route) + " - " + \
            str(self.departure_time)

    class Meta:
        verbose_name = 'Рейс'
        verbose_name_plural = 'Рейсы'
        ordering = ['departure_time']
        unique_together = ['route', 'departure_time']


class Bus(models.Model):
    registration_number = models.CharField(
        'Регистрационный номер',
        max_length=10,
        primary_key=True,
    )

    mark = models.CharField(
        'Марка',
        max_length=100
    )

    amount_of_places = models.PositiveSmallIntegerField(
        'Число мест',
    )

    driver = models.OneToOneField(
        'Driver',
        on_delete=models.PROTECT,
        verbose_name='Водитель',
    )

    def __str__(self):
        return f'{self.mark} {self.registration_number}'

    class Meta:
        verbose_name = 'Автобус'
        verbose_name_plural = 'Автобусы'
        ordering = ['mark']


class Driver(models.Model):
    passport_number = models.CharField(
        'Номер паспорта',
        max_length=25,
        unique=True,
    )

    name = models.CharField(
        'Имя',
        max_length=255
    )

    second_name = models.CharField(
        'Фамилия',
        max_length=255
    )

    middle_name = models.CharField(
        'Отчество',
        max_length=255
    )

    phone_number = models.BigIntegerField(
        'Номер телефона',
        unique=True,
        validators=[MinValueValidator(1)]
    )

    age = models.PositiveSmallIntegerField(
        'Возраст',
        validators=[MinValueValidator(21)]
    )

    def __str__(self): return str(self.second_name) + " " + \
        str(self.name[0]) + "." + \
        str(self.middle_name[0]) + ". - " + \
        str(self.passport_number)

    class Meta:
        verbose_name = 'Водитель'
        verbose_name_plural = 'Водители'
        ordering = ['name', 'second_name', 'middle_name']


class Ticket(models.Model):
    flight = models.ForeignKey(
        'Flight',
        on_delete=models.PROTECT,
        verbose_name='Рейс',
    )

    user = models.CharField(
        'Покупатель',
        max_length=255
    )

    seller = models.CharField(
        'Продавец',
        max_length=255
    )

    registration_time = models.DateTimeField(
        'Время оформления',
        auto_now_add=True,
    )

    def __str__(self):
        return str(self.flight) + \
            " - " + \
            str(self.user)

    class Meta:
        verbose_name = 'Билет'
        verbose_name_plural = 'Билеты'
        ordering = ['flight']
        get_latest_by = 'registration_time'
