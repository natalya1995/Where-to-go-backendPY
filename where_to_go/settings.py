from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent


DEBUG = False 
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'change-me-for-local-only')
ALLOWED_HOSTS = ['wheretogo.pythonanywhere.com']  

CSRF_TRUSTED_ORIGINS = ['https://wheretogo.pythonanywhere.com']

# --- Приложения ---
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'corsheaders',
    'django_filters',
    'places',
    'adminsortable2',
    'django_summernote',
]

# --- Middleware (ВАЖНО: corsheaders выше CommonMiddleware) ---
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # ← подняли выше
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'where_to_go.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # добавишь, если будут свои шаблоны вне apps
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'where_to_go.wsgi.application'

# --- БД ---
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# --- Пароли ---
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# --- Локаль/время ---
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'      # можно поменять на 'Asia/Almaty', если хочешь
USE_I18N = True
USE_TZ = True

# --- Статика/медиа (папки с точкой — норм, просто чуть «скрытые») ---
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / '.static'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / '.media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}

# --- CORS ---
CORS_ALLOW_ALL_ORIGINS = False
CORS_ALLOWED_ORIGINS = [
     "https://твойдомен.ком",
     "https://wheretogo.pythonanywhere.com",
 ]

# Лайфхак для Summernote, если нужны iframe:
X_FRAME_OPTIONS = 'SAMEORIGIN'
