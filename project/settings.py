"""
Django settings for contactsapi project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

"""
create a virtual environment and activate
pip install -r requirements.txt 

rest_framework
- ModelSerializer 
- permissions 

"""

from pathlib import Path
import dotenv
import os 
import django_heroku 


# export variables  in .env file   $ export -p 
dotenv.load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
APPEND_SLASH=True 


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# when DEBUG = False, then set ALLOWED_HOSTS 
ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework', 
    'auths',
    'ballers', 
    'drf_yasg',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

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

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_USER_MODEL = "auths.NewUser"


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

CORS_ORIGIN_WHITELIST = [
    'http://localhost:3000', 
    'http://127.0.0.1:8080',
]


REST_FRAMEWORK ={
    'DEFAULT_AUTHENTICATION_CLASSES':(
        'auths.backends.JWTAuthentication', 
    ), 
    'DEFAULT_PERMISSION_CLASSES': [ 
        'rest_framework.permissions.AllowAny'
    ]
}

#JWT 
JWT_SECRET_KEY=os.environ.get("JWT_SECRET_KEY") 

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'


#HEROKU : When Debug = False, it comes into effect (error: if localhost)
django_heroku.settings(locals())


# SWAGGER ( drf_yasg )
SWAGGER_SETTINGS={
    'SECURITY_DEFINITIONS':{
        "Authorization Token eg [Bearer (jwt_token) ]": {
            "type": "apiKey", 
            "name": "Authorization", 
           "in":  "header"
        }
    }, 
        'DEFAULT_MODEL_DEPTH': -1
}

LOGIN_URL = "/"



"""
To change django authentication model 
- delete previous migrations and drop table 
- INSTALLED_APPS = [ ...., "auths"]
- AUTH_USER_MODEL = "auths.NewUser"
-  python manage.py makemigration auths 
- python manage.py migrate 

postman: type: bearer token    
        provide token without quotations)   #it sends  b' Bearer xxx'
$ curl -X GET "http://127.0.0.1:5000/api/contacts"  -H  "Authorization: Bearer  xxx"

"""