# drf-jwt_template

1. Реализована аутентификация на основании токенов JWT (библиотека [djangorestframework-simplejwt](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html)).
2. Эндпоинты аутентификации реализованы с помощью библиотеки [djoser](https://djoser.readthedocs.io/en/latest/getting_started.html).
3. Подключен Swagger (OpenAPI 3.0, использован [drf-spectacular](https://drf-spectacular.readthedocs.io/en/latest/), статика для api добавлена через [drf-spectacular-sidecar](https://drf-spectacular.readthedocs.io/en/latest/readme.html)).
4. Подключен [ruff](https://docs.astral.sh/ruff/), настройки в pyproject.toml.
5. Подключены [django-filters](https://django-filter.readthedocs.io/en/main/).
6. Обратите внимание, в проекте использован Django 5.2.

## Настройки

- Добавлен тротлинг запросов, настойка в settings.py -> REST_FRAMEWORK.
- Доступ до дефолту - IsAuthenticatedOrReadOnly.
- Прописан шаблон кастомного обработчика ошибок (404), добавление новых в api/exceptions.py.
- Пагинация по дефолту - PageNumberPagination.
- Переопределен AbstractUser, добавлены поля created_at и updated_at, поле email сделано обязательным.
