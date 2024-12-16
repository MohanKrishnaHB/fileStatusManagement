import os
from .settings import *
from .settings import BASE_DIR

SECRET_KEY = os.environ['SECRET']
ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']]
CSRF_TRUSTED_ORIGINS = ['https://'+os.environ['WEBSITE_HOSTNAME']]
DEBUG = True


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': os.environ['AZURE_MYSQL_HOST'],
        'NAME': os.environ['AZURE_MYSQL_NAME'],
        'USER': os.environ['AZURE_MYSQL_USER'],
        'PASSWORD': os.environ['AZURE_MYSQL_PASSWORD']
    }
}

AUTH_USER_MODEL = 'client.CustomUser'

LOGIN_URL = 'client:login'
LOGIN_REDIRECT_URL = 'file:dashboard'
LOGOUT_REDIRECT_URL = 'client:login'