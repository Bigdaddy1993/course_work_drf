from rest_framework import serializers

from habit.models import Habit
from habit.validators import (
    ExceptionHabitValidator,
    RelatedHabitValidator,
    DateHabitValidator,
    NiceHabitValidator,
    PeriodHabitValidator,
)


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = "__all__"
        validators = [
            ExceptionHabitValidator("related_habit", "reward"),
            RelatedHabitValidator("related_habit"),
            NiceHabitValidator("related_habit", "reward", "is_useful_habits"),
            DateHabitValidator("time_to_complete"),
            PeriodHabitValidator("periods"),
        ]
