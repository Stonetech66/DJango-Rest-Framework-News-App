"""
Django settings for Blogappx project.

Generated by 'django-admin startproject' using Django 2.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
from decouple import config
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY =config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
CORS_ALLOW_ALL_ORIGINS= True
CORS_URLS_REGEX= r"^/api/.*$"


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    # Third party app  
   
    'rest_framework',
    'corsheaders',
    'rest_framework.authtoken',
    'rest_framework_simplejwt',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',

    'dj_rest_auth',
    'dj_rest_auth.registration',
    'django_filters',
#
    'rest_framework_swagger',


    #Local Apps
    'Users.apps.UsersConfig',
    'Blog.apps.BlogConfig',

]
#allauth
SITE_ID= 1

AUTH_USER_MODEL= 'Users.CustomUsers'

ACCOUNT_UNIQUE_EMAIL= True

ACCOUNT_EMAIL_REQUIRED= True

ACCOUNT_AUTHENTICATION_METHOD= 'username_email'

ACCOUNT_LOGIN_ATTEMPTS_LIMIT= 5


ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT= 300

ACCOUNT_EMAIL_VERIFICATION= "optional"



AUTHENTICATION_BACKENDS= (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend")

# Email Settings


EMAIL_BACKEND= 'django.core.mail.backends.console.EmailBackend'






MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Blogappx.urls'

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

WSGI_APPLICATION = 'Blogappx.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': 'postgres',
        'PASSWORD':config('DB_PASSWORD'),
        'HOST':config('DB_HOST'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT='static'

#media
MEDIA_URL= '/media/'
MEDIA_ROOT='media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#Third Party App

REST_FRAMEWORK= {
     "DEFAULT_AUTHENTICATION_CLASSES":[
        "dj_rest_auth.jwt_auth.JWTCookieAuthentication"
    ],
    "DEFAULT_PERMISSION_CLASSES":[
        "rest_framework.permissions.IsAuthenticatedOrReadOnly"
    ],

    "DEFAULT_PAGINATION_CLASS": 'rest_framework.pagination.LimitOffsetPagination',
    "PAGE_SIZE": 4,

    'DEFAULT_SCHEMA_CLASS':'rest_framework.schemas.AutoSchema',
    
}

REST_USE_JWT= True
JWT_AUTH_COOKIE='blog-auth'
JWT_AUTH_REFRESH_COOKIE= 'my-blog-refresh-cookie'
OLD_PASSWORD_FIELD_ENABLED= True

REST_AUTH_REGISTER_SERIALIZERS={
    "REGISTER_SERIALIZER":'Blog.serializers.RegisterSerailizer'
}

REST_AUTH_SERIALIZERS={
    "USER_DETAILS_SERIALIZER":'Blog.serializers.UserAccountSerializer'
}


