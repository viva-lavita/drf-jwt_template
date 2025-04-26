from djoser.views import UserViewSet as DjoserUserViewSet
from rest_framework import permissions, status
from rest_framework.response import Response


class UserViewSet(DjoserUserViewSet):
    def get_permissions(self):
        if self.action == "me":
            self.permission_classes = (permissions.IsAuthenticated,)
        return super().get_permissions()

    def retrieve(self, request, *args, **kwargs):
        """
        Доступ только для авторизованных пользователей.

        Пользователь может получить только cвой профиль.
        Любой профиль может посмотреть только админ.
        """
        return super().retrieve(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        """
        Доступ только для авторизованных пользователей.

        Любой профиль может посмотреть только админ.
        Авторизованный пользователь может посмотреть свой профиль.
        """
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """Доступ только для неавторизованных пользователей."""
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """
        Доступ только для авторизованных пользователей.

        Пользователь может обновить свой профиль.
        Любой профиль может обновить только админ.
        """
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """
        Доступ только для авторизованных пользователей.

        Пользователь может обновить свой профиль.
        Любой профиль может обновить только админ.
        """
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        Доступ только для авторизованных пользователей.

        Пользователь может удалить свой профиль.
        Любой профиль может удалить только админ.
        """
        # переопределено, т.к. требовался текущий пароль в теле запроса
        # тело при delete методе не одобряется OpenAPI
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
