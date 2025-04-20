from django.contrib.auth import get_user_model
from django.db.models import Q
from djoser.serializers import UserCreatePasswordRetypeSerializer as DjoserUserCreateSerializer
from djoser.serializers import UserSerializer as DjoserUserSerializer
from rest_framework import serializers

User = get_user_model()


class UserSerializer(DjoserUserSerializer):
    """
    Базовый сериализатор пользователя для всех action кроме 'create'.

    Выводится максимальная информация о пользователе.
    При редактировании пользователя проверяется уникальность новых email и
    username, если эти поля будут изменены.
    """
    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'username',
            'first_name',
            'last_name',
            'created_at',
            'updated_at',
        )

    def get_validate_duplicate(self, field):
        request = self.context.get('request')
        value = request.data.get(field)
        if value and request.method in ('PUT', 'PATCH'):
            user_id = request.user.id
            users = User.objects.filter(
                Q(email=value) & ~Q(id=user_id)).all()
            if users:
                return f'Пользователь с таким {field} уже существует'

    def validate_email(self, value):
        error = self.get_validate_duplicate('email')
        if error:
            raise serializers.ValidationError(error)
        return value

    def validate_username(self, value):
        error = self.get_validate_duplicate('username')
        if error:
            raise serializers.ValidationError(error)
        return value


class UserCreateSerializer(DjoserUserCreateSerializer):
    """
    Сериализатор создания пользователя.
    """
    password = serializers.CharField(write_only=True)
    re_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'password',
            're_password',
        )

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                'Пользователь с таким email уже существует')
        return value

    def validate_username(self, value):
        if value and User.objects.filter(username=value).exists():
            raise serializers.ValidationError(
                'Пользователь с таким username уже существует')
        return value

    def validate_password(self, value):
        from django.contrib.auth.password_validation import validate_password
        validate_password(value)
        return value

    def validate_re_password(self, value):
        if self.initial_data['password'] != value:
            raise serializers.ValidationError('Пароли не совпадают')
        return value


class ShortReadUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
        )


class EmptySerializer(serializers.Serializer):
    pass
