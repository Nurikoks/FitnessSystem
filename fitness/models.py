from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    birthday = models.DateField(null=True, blank=True, verbose_name="Дата рождения")

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return (
            f"{self.username} ({', '.join(group.name for group in self.groups.all())})"
        )


class Trainer(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, verbose_name="Пользователь"
    )

    class Meta:
        verbose_name = "Тренер"
        verbose_name_plural = "Тренеры"

    def __str__(self):
        return self.user.get_full_name() or self.user.username


class Gym(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    address = models.CharField(max_length=255, verbose_name="Адрес")

    class Meta:
        verbose_name = "Зал"
        verbose_name_plural = "Залы"

    def __str__(self):
        return self.name


class TrainersGym(models.Model):
    trainer = models.ForeignKey(
        Trainer, on_delete=models.CASCADE, related_name="gyms", verbose_name="Тренер"
    )
    gym = models.ForeignKey(
        Gym, on_delete=models.CASCADE, related_name="trainers", verbose_name="Зал"
    )

    class Meta:
        verbose_name = "Тренер-зал"
        verbose_name_plural = "Тренеры-залы"

    def __str__(self):
        return f"{self.trainer} - {self.gym}"


class Schedule(models.Model):
    DAYS = [
        ("MON", "Понедельник"),
        ("TUE", "Вторник"),
        ("WED", "Среда"),
        ("THU", "Четверг"),
        ("FRI", "Пятница"),
        ("SAT", "Суббота"),
        ("SUN", "Воскресенье"),
    ]

    trainer = models.ForeignKey(
        Trainer,
        on_delete=models.CASCADE,
        related_name="schedules",
        verbose_name="Тренер",
    )
    gym = models.ForeignKey(
        Gym, on_delete=models.CASCADE, related_name="schedules", verbose_name="Зал"
    )
    day_of_week = models.CharField(
        max_length=3, choices=DAYS, verbose_name="День недели"
    )
    start_time = models.TimeField(verbose_name="Время начала")
    end_time = models.TimeField(verbose_name="Время окончания")

    class Meta:
        verbose_name = "Расписание"
        verbose_name_plural = "Расписания"

    def __str__(self):
        return f"{self.get_day_of_week_display()} {self.start_time}-{self.end_time}"


class Booking(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="bookings",
        verbose_name="Пользователь",
    )
    schedule = models.ForeignKey(
        Schedule,
        on_delete=models.CASCADE,
        related_name="bookings",
        verbose_name="Расписание",
    )
    booking_date = models.DateField(verbose_name="Дата записи")
    booking_time = models.TimeField(verbose_name="Время записи")
    duration_hours = models.IntegerField(verbose_name="Длительность (часы)")

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"

    def __str__(self):
        return f"Запись {self.booking_date} {self.booking_time} ({self.user.username})"
