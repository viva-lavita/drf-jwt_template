import os
import sys
from pathlib import Path
from platform import system

from dotenv import load_dotenv

try:
    load_dotenv(os.path.join(Path(__file__).resolve().parent.parent.parent, '.env'))
except FileNotFoundError:
    raise FileNotFoundError('Did not find .env')

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = os.getenv('DEBUG', default=False) == 'True'

ALLOWED_HOSTS = os.getenv(
    'ALLOWED_HOSTS', '127.0.0.1 localhost'
).split()

CSRF_TRUSTED_ORIGINS = os.getenv(
    'CSRF_TRUSTED_ORIGINS', 'http://127.0.0.1 http://localhost'
).split()

CORS_ALLOWED_ORIGINS = os.getenv(
    'CORS_ALLOWED_ORIGINS', 'http://127.0.0.1 http://localhost'
).split()

CSRF_COOKIE_SECURE = os.getenv('CSRF_COOKIE_SECURE', default=False) == 'True'

SESSION_COOKIE_SECURE = os.getenv('SESSION_COOKIE_SECURE', default=False) == 'True'

DEFAULT_SITE_URL = os.getenv('DEFAULT_SITE_URL', default='127.0.0.1:8000')

OPERATING_SYSTEM = system()

# Application definition

# base
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

# packages
INSTALLED_APPS += [
    "rest_framework",
    "rest_framework_simplejwt",
    "rest_framework.authtoken",
    "django_filters",
    "djoser",
    "corsheaders",
    "drf_spectacular",
    "drf_spectacular_sidecar",
]

# apps
INSTALLED_APPS += [
    "api.apps.ApiConfig",
    "users.apps.UsersConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


########################
#  STATIC AND MEDIA
########################
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


ENABLE_DEBUG_TOOLBAR = DEBUG and "test" not in sys.argv
if ENABLE_DEBUG_TOOLBAR:
    INSTALLED_APPS.append("debug_toolbar")
    MIDDLEWARE.append("debug_toolbar.middleware.DebugToolbarMiddleware")


########################
#  API
########################
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],

    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend'
    ],
    'EXCEPTION_HANDLER': 'api.exceptions.custom_exception_handler',
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 30
}


########################
#  SWAGGER
########################
SPECTACULAR_SETTINGS = {
    'TITLE': 'Django5 Template',
    'DESCRIPTION': 'Django5 Test Swagger API description',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    'SCHEMA_PATH_PREFIX': '/api/v1/',
    'COMPONENT_SPLIT_REQUEST': True,
    'SWAGGER_UI_SETTINGS': {
        'deepLinking': True,
        'persistAuthorization': True,
    },
    'SWAGGER_UI_DIST': 'SIDECAR',
    'SWAGGER_UI_FAVICON_HREF': 'SIDECAR',
    'REDOC_DIST': 'SIDECAR',
}

#######################
#  USER
#######################
DJOSER = {
    'LOGIN_FIELD': 'email',
    'USERNAME_FIELD': 'email',
    'USER_CREATE_PASSWORD_RETYPE': True,
    'SEND_ACTIVATION_EMAIL': False,
    'PASSWORD_CHANGED_EMAIL_CONFIRMATION': False,
    'PASSWORD_RESET_CONFIRM_RETYPE': False,
    'HIDE_USERS': False,
    "PASSWORD_RESET_CONFIRM_URL": "#/password/reset/confirm/{uid}/{token}",  # в письмах настроить
    "USERNAME_RESET_CONFIRM_URL": "#/username/reset/confirm/{uid}/{token}",
    'SERIALIZERS': {
        'user': 'users.serializers.UserSerializer',
        'current_user': 'users.serializers.UserSerializer',
        'user_create_password_retype': 'users.serializers.UserCreateSerializer',
    },
    'PERMISSIONS': {
        'user': ('api.permissions.AuthorOrStaff',),
        'user_list': ('rest_framework.permissions.IsAdminUser',),
        'token_destroy': ('rest_framework.permissions.IsAuthenticated',),
        'user_create': ('api.permissions.NotIsAuthenticated',),
    },
    # 'DEFAULT_PARSER_CLASSES': (
    #     'rest_framework.parsers.JSONParser',
    #     'rest_framework.parsers.FormParser',
    #     'rest_framework.parsers.MultiPartParser',
    # )
}
