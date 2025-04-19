from django.urls import include, path
from rest_framework.routers import DefaultRouter
from djoser.views import TokenCreateView

from .views import TokenDestroyView, UserViewSet


app_name = "users"


router = DefaultRouter()
router.register("users", UserViewSet, basename="users")


urlpatterns = [
    path("", include(router.urls)),
    path('token/login/', TokenCreateView.as_view(), name="login"),
    path('token/logout/', TokenDestroyView.as_view(), name="logout"),
]
