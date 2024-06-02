from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from users.apps import UsersConfig
from users.views import (
    UserCreateApiView,
    UserUpdateAPIView,
    UserRetrieveAPIView,
    UserDeleteAPIView,
)

app_name = UsersConfig.name

urlpatterns = [
    path("register/", UserCreateApiView.as_view(), name="register_user"),
    path("update/<int:pk>/", UserUpdateAPIView.as_view(), name="update_user"),
    path("<int:pk>/", UserRetrieveAPIView.as_view(), name="get_user"),
    path("delete/<int:pk>/", UserDeleteAPIView.as_view(), name="delete_user"),
    path("token/", TokenObtainPairView.as_view(), name="token"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
