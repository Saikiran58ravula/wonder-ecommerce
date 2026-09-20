```python
"""
Django settings for wonder_core project.
"""

from pathlib import Path

from decouple import config
import dj_database_url


# ============================================================
# BASE DIRECTORY
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent


# ============================================================
# SECURITY
# ============================================================

# SECRET_KEY is loaded from the .env file.
SECRET_KEY = config('SECRET_KEY')

# True for local development, False for production.
DEBUG = config('DEBUG', default=False, cast=bool)

# Example:
# ALLOWED_HOSTS=127.0.0.1,localhost
ALLOWED_HOSTS = config(
    'ALLOWED_HOSTS',
    default='127.0.0.1,localhost',
    cast=lambda value: [
        host.strip()
        for host in value.split(',')
        if host.strip()
    ]
)


# ============================================================
# APPLICATIONS
# ============================================================

INSTALLED_APPS = [

    # --------------------------------------------------------
    # Django built-in apps
    # --------------------------------------------------------
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',

    # --------------------------------------------------------
    # Cloudinary
    # --------------------------------------------------------
    'cloudinary_storage',
    'django.contrib.staticfiles',
    'cloudinary',

    # --------------------------------------------------------
    # Wonder apps
    # --------------------------------------------------------
    'accounts',
    'products',
    'cart',
    'orders',
]


# ============================================================
# MIDDLEWARE
# ============================================================

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    # Serve static files efficiently in production
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',

    'django.middleware.common.CommonMiddleware',

    'django.middleware.csrf.CsrfViewMiddleware',

    'django.contrib.auth.middleware.AuthenticationMiddleware',

    'django.contrib.messages.middleware.MessageMiddleware',

    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# ============================================================
# URL CONFIGURATION
# ============================================================

ROOT_URLCONF = 'wonder_core.urls'


# ============================================================
# TEMPLATES
# ============================================================

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        # Main Wonder templates folder
        'DIRS': [
            BASE_DIR / 'templates',
        ],

        # Also search inside each app's templates folder
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


# ============================================================
# WSGI
# ============================================================

WSGI_APPLICATION = 'wonder_core.wsgi.application'


# ============================================================
# DATABASE
# ============================================================

# Local development:
#     SQLite will be used automatically if DATABASE_URL
#     is not present.
#
# Production:
#     DATABASE_URL can point to PostgreSQL or another
#     supported database.

DATABASES = {
    'default': dj_database_url.config(
        default=f'sqlite:///{BASE_DIR / "db.sqlite3"}',
        conn_max_age=600,
    )
}


# ============================================================
# PASSWORD VALIDATION
# ============================================================

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME':
            'django.contrib.auth.password_validation.'
            'UserAttributeSimilarityValidator',
    },
    {
        'NAME':
            'django.contrib.auth.password_validation.'
            'MinimumLengthValidator',
    },
    {
        'NAME':
            'django.contrib.auth.password_validation.'
            'CommonPasswordValidator',
    },
    {
        'NAME':
            'django.contrib.auth.password_validation.'
            'NumericPasswordValidator',
    },
]


# ============================================================
# INTERNATIONALIZATION
# ============================================================

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True


# ============================================================
# STATIC FILES
# ============================================================

# URL used by Django for static files.
STATIC_URL = '/static/'

# Local development static folder.
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# Folder created by:
# python manage.py collectstatic
STATIC_ROOT = BASE_DIR / 'staticfiles'

# WhiteNoise storage.
STATICFILES_STORAGE = (
    'whitenoise.storage.CompressedManifestStaticFilesStorage'
)


# ============================================================
# MEDIA FILES
# ============================================================

# Product images and other uploaded media will be stored
# using Cloudinary.

MEDIA_URL = '/media/'

DEFAULT_FILE_STORAGE = (
    'cloudinary_storage.storage.MediaCloudinaryStorage'
)


# ============================================================
# CLOUDINARY
# ============================================================

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': config('CLOUDINARY_CLOUD_NAME'),

    'API_KEY': config('CLOUDINARY_API_KEY'),

    'API_SECRET': config('CLOUDINARY_API_SECRET'),
}


# ============================================================
# AUTHENTICATION REDIRECTS
# ============================================================

# After successful login
LOGIN_REDIRECT_URL = 'products:home'

# After logout
LOGOUT_REDIRECT_URL = 'products:home'

# Where unauthenticated users are redirected
LOGIN_URL = 'accounts:login'


# ============================================================
# RAZORPAY
# ============================================================

# Razorpay credentials are stored in the .env file.

RAZORPAY_KEY_ID = config(
    'RAZORPAY_KEY_ID',
    default=''
)

RAZORPAY_KEY_SECRET = config(
    'RAZORPAY_KEY_SECRET',
    default=''
)


# ============================================================
# CSRF / DEPLOYMENT
# ============================================================

# For local development, this can remain empty.
#
# In production, you can configure:
#
# CSRF_TRUSTED_ORIGINS=https://yourdomain.com
#
# Multiple domains can be separated by commas.

CSRF_TRUSTED_ORIGINS = config(
    'CSRF_TRUSTED_ORIGINS',
    default='',
    cast=lambda value: [
        origin.strip()
        for origin in value.split(',')
        if origin.strip()
    ]
)


# ============================================================
# DEFAULT PRIMARY KEY
# ============================================================

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
```
