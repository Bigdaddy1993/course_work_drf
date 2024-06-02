from django.db import models
from config import settings

NULLABLE = {"blank": True, "null": True}


class Habit(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        **NULLABLE,
    )
    place = models.CharField(max_length=20, verbose_name="Место выполнения")
    time = models.TimeField(default="00:00:00", verbose_name="Время выполнения")
    action_habit = models.CharField(
        max_length=20, verbose_name="Действие по представлению привычки"
    )
    is_useful_habits = models.BooleanField(
        default=False, verbose_name="Признак полезной привычки"
    )
    related_habit = models.ForeignKey(
        "self", on_delete=models.CASCADE, verbose_name="Связанная привычка", **NULLABLE
    )
    periods = models.PositiveSmallIntegerField(default=1, verbose_name="Период")
    reward = models.CharField(max_length=100, verbose_name="Вознаграждение", **NULLABLE)
    time_to_complete = models.PositiveSmallIntegerField(
        default=60, verbose_name="Время на выполнение"
    )
    is_public = models.BooleanField(default=True, verbose_name="Признак публикации")

    def __str__(self):
        return f"{self.action}"

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
