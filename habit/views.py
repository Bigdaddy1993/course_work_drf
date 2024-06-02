from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from rest_framework.permissions import IsAuthenticated

from habit.models import Habit
from habit.paginators import HabitPaginator
from habit.permissions import IsUser
from habit.serializers import HabitSerializer


class HabitCreateApiView(CreateAPIView):
    """Создание привычки"""

    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = serializer.save()
        user.user = self.request.user
        user.save()


class UserHabitListApiView(ListAPIView):
    """Получения списка привычек текущего пользователя"""

    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class HabitListApiView(ListAPIView):
    """Список публичных привычек"""

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    pagination_class = HabitPaginator
    permission_classes = [IsAuthenticated, IsUser]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class HabitRetrieveApiView(RetrieveAPIView):
    """Список привычек текущего пользователя с пагинацией"""

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsUser]


class HabitUpdateApiView(UpdateAPIView):
    """Редактирование привычки"""

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsUser]


class HabitDestroyApiView(DestroyAPIView):
    """Удаление привычки"""

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsUser]
