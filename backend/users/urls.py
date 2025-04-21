from django.urls import include, path
from djoser.views import TokenCreateView
from rest_framework.routers import DefaultRouter

from .views import TokenDestroyView, UserViewSet

app_name = "users"


router = DefaultRouter()
router.register("users", UserViewSet, basename="users")


urlpatterns = [
    path("", include(router.urls)),
    path("", include("djoser.urls.jwt")),
    path("token/login/", TokenCreateView.as_view(), name="login"),
    path("token/logout/", TokenDestroyView.as_view(), name="logout"),
]
