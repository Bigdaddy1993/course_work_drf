from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from habit.models import Habit
from users.models import User


class HabitTestCase(APITestCase):
    def setUp(self):
        """
        Устанавливаем начальные данные для тестов.
        Создаем двух пользователей и одну привычку.
        """
        self.user = User.objects.create(email="smth@mail.com", is_superuser=True)

        self.client.force_authenticate(user=self.user)

        self.habit = Habit.objects.create(place="place", action_habit="something")

    def test_get_list(self):

        url = reverse("habit:list_habit")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_habit(self):
        data = {
            "place": self.habit.place,
            "user": self.user.id,
            "action_habit": self.habit.action_habit,
        }
        url = reverse("habit:create_habit")
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Habit.objects.all().exists())
        self.assertEqual(response.json()["place"], data["place"])
        self.assertEqual(response.json()["action_habit"], data["action_habit"])

    def test_update_habit(self):
        habit = Habit.objects.create(
            user=self.user,
            place="Test",
            action_habit="Test",
            is_useful_habits=True,
            periods=1,
        )
        data_habit_change = {
            "name": "Test_1",
        }
        response = self.client.patch(
            reverse("habit:update_habit", kwargs={"pk": habit.pk}),
            data=data_habit_change,
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_habit(self):
        habit = Habit.objects.create(
            user=self.user,
            place="Test",
            action_habit="Test",
            is_useful_habits=True,
            periods=1,
        )
        response = self.client.delete(
            reverse("habit:delete_habit", kwargs={"pk": habit.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
