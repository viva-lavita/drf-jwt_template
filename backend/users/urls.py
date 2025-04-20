from django.urls import include, path
from djoser.views import TokenCreateView
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from .views import TokenDestroyView, UserViewSet

app_name = "users"


router = DefaultRouter()
router.register("users", UserViewSet, basename="users")


urlpatterns = [
    path("", include(router.urls)),
    path("", include("djoser.urls.jwt")),
    # path('token/login/', TokenCreateView.as_view(), name="login"),
    # path('token/logout/', TokenDestroyView.as_view(), name="logout"),
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
