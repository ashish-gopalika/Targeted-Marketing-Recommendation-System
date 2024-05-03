from .base import *
from .base import env


env.read_env(str(BASE_DIR / ".envs" / ".local"))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
DOMAIN = "localhost:8000"
ALLOWED_HOSTS = ['*','localhost:8000','django']

CSRF_TRUSTED_ORIGINS = [
    'http://localhost:8000'
]

DOMAIN = 'localhost:8000'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('POSTGRES_DB'),
        'USER': env('POSTGRES_USER'),
        'PASSWORD': env('POSTGRES_PASSWORD'),
        'HOST': env('POSTGRES_HOST'),
        'PORT': env('POSTGRES_PORT')
    }
}
