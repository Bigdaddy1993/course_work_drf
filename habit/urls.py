from django.urls import path

from habit.apps import HabitConfig
from habit.views import (
    HabitCreateApiView,
    HabitListApiView,
    HabitRetrieveApiView,
    HabitUpdateApiView,
    HabitDestroyApiView,
    UserHabitListApiView,
)

app_name = HabitConfig.name

urlpatterns = [
    path("habit/create/", HabitCreateApiView.as_view(), name="create_habit"),
    path("habit/", HabitListApiView.as_view(), name="list_habit"),
    path("habit/<int:pk>/", HabitRetrieveApiView.as_view(), name="get_habit"),
    path("habit/update/<int:pk>/", HabitUpdateApiView.as_view(), name="update_habit"),
    path("habit/delete/<int:pk>/", HabitDestroyApiView.as_view(), name="delete_habit"),
    path("habit/public/", UserHabitListApiView.as_view(), name="public"),
]
