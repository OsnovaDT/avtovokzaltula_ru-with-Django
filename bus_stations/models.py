from django.db import models


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

    stopover = models.CharField(
        'Остановки',
        max_length=255,
        null=True,
        blank=True,
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
        return self.name

    class Meta:
        verbose_name = 'Маршрут'
        verbose_name_plural = 'Маршруты'
        ordering = ['name']


class Flight(models.Model):
    bus_station = models.ForeignKey(
        'BusStation',
        on_delete=models.CASCADE,
        verbose_name='Автовокзал'
    )

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

    bus = models.OneToOneField(
        'Bus',
        on_delete=models.CASCADE,
        verbose_name='Автобус',
    )

    def __str__(self):
        return f'{self.bus_station} - {self.route}'

    class Meta:
        verbose_name = 'Рейс'
        verbose_name_plural = 'Рейсы'
        ordering = ['departure_time']
        unique_together = ['bus_station', 'route', 'departure_time']


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

    phone_number = models.CharField(
        'Номер телефона',
        max_length=15,
        unique=True,
    )

    age = models.PositiveSmallIntegerField(
        'Возраст',
    )

    bus = models.OneToOneField(
        'Bus',
        on_delete=models.CASCADE,
        verbose_name='Автобус'
    )

    def __str__(self):
        return f'{self.second_name} {self.name}[0].\
            {self.middle_name}[0]. - {self.passport_number}'

    class Meta:
        verbose_name = 'Водитель'
        verbose_name_plural = 'Водители'
        ordering = ['name', 'second_name', 'middle_name']
