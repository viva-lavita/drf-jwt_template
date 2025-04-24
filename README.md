# drf-jwt_template

Шаблон для нового проекта Django с JWT аутентификацией. Django использован 5 версии.

## Инструменты

1. Реализована аутентификация на основании токенов JWT (библиотека [djangorestframework-simplejwt](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html)).
2. Эндпоинты аутентификации реализованы с помощью библиотеки [djoser](https://djoser.readthedocs.io/en/latest/getting_started.html).
3. Подключен Swagger (OpenAPI 3.0, использован [drf-spectacular](https://drf-spectacular.readthedocs.io/en/latest/), статика для api добавлена через [drf-spectacular-sidecar](https://drf-spectacular.readthedocs.io/en/latest/readme.html)).
4. Подключен [ruff](https://docs.astral.sh/ruff/), настройки в pyproject.toml.
5. Подключены [django-filters](https://django-filter.readthedocs.io/en/main/).
6. В dev зависимости добавлены и настроены [pre-commit](https://pre-commit.com/) и [django-debug-toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/installation.html).
7. Добавлены файлы [docker](https://docs.docker.com/build/) и [docker-compose](https://docs.docker.com/compose/) (dev и prod версии).

## Настройки

- Добавлен тротлинг запросов, настойка в settings.py -> REST_FRAMEWORK.
- Доступ до дефолту - IsAuthenticatedOrReadOnly.
- Прописан шаблон кастомного обработчика ошибок (404), добавление новых в api/exceptions.py.
- Пагинация по дефолту - PageNumberPagination.
- Переопределен AbstractUser, добавлены поля created_at и updated_at, поле email сделано обязательным.

### Перевод

Использование:

```python
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    email = models.EmailField(
        verbose_name='Email',
        max_length=254,
        unique=True,
        help_text=_(
            "Required. 254 characters or fewer. "
            "Letters, digits and @/./+/-/_ only."
        ),
        error_messages={
            "unique": _("A user with that email already exists."),
        },
    )
```

Для формирования файла перевода на русском используйте [команду](https://docs.djangoproject.com/en/5.2/ref/django-admin/#django-admin-makemessages):

```bash
django-admin makemessages --locale=ru
```

В файле backend/locale/ru/LC_MESSAGES/django.po пропишите переводы помеченных фраз и скомпилируйте итоговый .mo файл:

```bash
python manage.py compilemessages -l ru
```

Локаль меняется в settings.py в разделе INTERNATIONALIZATION. [Документация](https://docs.djangoproject.com/en/4.2/topics/i18n/)

### ENV

Для генерации секретных ключей вы можете выполнить следующую команду:

```bash
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

ДОПИСАТЬ

### docker-compose

В проекте два docker-compose файла -  для дев и прод версий. Обратите внимание, если для локальной разработке в контейнерах вы захотите сделать двухстороннюю синхронизацию, чтобы изменения в коде прогружались в контейнер и наоборот, с текущей версией у вас ничего не получится, так как для образа используется uv, который создает виртуальную среду внутри контейнера, что создает коллизии и виртуальная среда не распознается.
Если вам очень нужен данный функционал, можно воспользоваться советами из [этого обсуждения](https://github.com/astral-sh/uv/issues/9423)

Команда пересборки dev-контейнеров:
```bash
docker compose -f docker-compose.dev.yml up --build
```

Команда для прод сборки:

```bash
docker compose up
```
