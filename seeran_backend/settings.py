from pathlib import Path
from datetime import timedelta
from decouple import config


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-1hrd@6u+u$0ouahd*z)v5ra+hu1nn&ljum=oh(r0i3noxbsg7i'


# aws config
# access keys 
AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''

# activates debug mode for the application
DEBUG = False


# SECURITY WARNING: don't run with debug turned on in production!
# sets the ip addresses the application can be hosted from
ALLOWED_HOSTS = ["*"] 


# Application definition
# a list of all installed apps
INSTALLED_APPS = [
    
    # django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # project apps 
    'authentication', # users/security/authentication
    'schools', # schools/locations/logos
    
    # third party apps
    'storages', # allows for application to read/write to s3 bucket
    'corsheaders', # handle cors 
]


# project middleware
# all project middleware
MIDDLEWARE = [
    
    # cors headers middleware
    'corsheaders.middleware.CorsMiddleware',
    
    # projects middleware
    'authentication.middleware.TokenValidationMiddleware', # middleware for token authentication and renewal
    
    # django middleware    
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# cors config
# origins/domains allowed to communicate with the application
if not DEBUG:
    CORS_ALLOWED_ORIGINS = [
        'https://www.seeran-grades.com',
        'https://server.seeran-grades.com',
        
        # Add other allowed origins as needed
    ]
    
CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
    'https://www.seeran-grades.com',
    'https://server.seeran-grades.com'
    
    # Add other allowed origins as needed
]


# cors credentials
# allows credentials (cookies, authorization headers, or TLS client certificates) to be sent in cross-origin requests.
CORS_ALLOW_CREDENTIALS = True 


# rest framework config
# default authentication method
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}


# applications default user model
# our custom user model 
AUTH_USER_MODEL = 'authentication.CustomUser'


# user authenticator
# our custom authentication backend
AUTHENTICATION_BACKENDS = [
    'authentication.auth_backends.EmailOrIdNumberModelBackend',
    'django.contrib.auth.backends.ModelBackend',
    # Add other authentication backends if needed
]


# simplejwt config
# simplejwt token settings
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),  # Short-lived access token (adjust as needed)
    'REFRESH_TOKEN_LIFETIME': timedelta(days=30),    # Longer-lived refresh token (adjust as needed)
    'ROTATE_REFRESH_TOKENS': False,                  # Set to True if you want to rotate refresh tokens
    
    'TOKEN_BLACKLIST_ENABLED': True,
    'TOKEN_BLACKLIST_MODEL': 'rest_framework_simplejwt.token_blacklist.BlacklistedToken',
    # Other settings (e.g., ALGORITHM, SIGNING_KEY, etc.) can be customized as well
}


# Caching config
# applications caching configuration
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://localhost:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}


# Database
# connection credentials for postgres rds instance
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'seeran_database',
        'USER': 'tsholo',
        'PASSWORD': 'N4Hoj5Mjrw4BEGvfWZAB',
        'HOST': 'seeran-database.cz4cqeskmn2k.af-south-1.rds.amazonaws.com',
        'PORT': '5432',
    }
}


# s3 bucket
# s3 bucket configuration
AWS_STORAGE_BUCKET_NAME = 'seeran-storage'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'


# Email sending config


# ssl config
# configures the application to commmunicate in https
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True


# static files (CSS, JavaScript, Images)
# static files location
STATIC_URL = 'https://%s/' % AWS_S3_CUSTOM_DOMAIN


# default settings 
# the rest are default django settigns
ROOT_URLCONF = 'seeran_backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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


# seeran_backend/settings.py
WSGI_APPLICATION = 'seeran_backend.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
