from rest_framework import permissions
from djoser.views import (
    TokenDestroyView as DjoserTokenDestroyView,
    UserViewSet as DjoserUserViewSet
)

from users.serializers import EmptySerializer


class TokenDestroyView(DjoserTokenDestroyView):
    """
    Переопределено из-за drf-spectacular, т.к. POST запрос без
    тела не поддерживается.
    """
    serializer_class = EmptySerializer
    pass


class UserViewSet(DjoserUserViewSet):
    def get_permissions(self):
        if self.action == 'me':
            self.permission_classes = (permissions.IsAuthenticated,)
        return super().get_permissions()
