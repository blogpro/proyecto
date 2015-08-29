# -*- encoding: utf-8 -*-
"""
Django settings for proyecto project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
RUTA_PROYECTO = os.path.dirname(os.path.realpath(__file__))

import socket
a = socket.gethostbyname(socket.gethostname())


if str(a) == '127.0.1.1':
    debug = True
    HOSTS = ['*']
    NAME = ''
    USER = ''
    PASSWORD = ''
    HOST = ''
else:
    debug = False  
    HOSTS = ['http://systab.herokuapp.com/','systab.herokuapp.com']

    #Bd
    NAME = 'd9d46qtftu68ki'
    USER = 'oithnhwamizxka'
    PASSWORD = '6OrH6cRnkAugNL44gxypx_SpdQ'
    HOST = 'ec2-23-21-187-45.compute-1.amazonaws.com'


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'x#3$8^e=cb+ny^!#0!k30t_m1n^29m(3z#)8n=lir_z7n3*7=@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = debug

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = HOSTS


#Editor
CKEDITOR_MEDIA_PREFIX = "/static/ckeditor/" #copiar ``media/ckeditor``
CKEDITOR_UPLOAD_PATH = "/media/"# Subir archivos
#CKEDITOR_JQUERY_URL = '/static/js/jquery-2.1.1.min.js'
CKEDITOR_CONFIGS = {
       'default': {
           'toolbar': 'Full',
           'height': 800,
           'width': 900,
           #'removePlugins': 'stylesheetparser',
           #'extraPlugins': 'codesnippet',
       },
   }
#Editor



# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'inicio',
    'etiquetas',
    'post',
    'votos',
    'comentarios',
    'respuestas',
    'categorias',
    'menu',

    'subtitulos',
    'descripciones',
    'codigos',
    'imagenes',

    'social.apps.django_app.default',#Login con facebook

    'ckeditor',
    'suit_ckeditor',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'proyecto.urls'

WSGI_APPLICATION = 'proyecto.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'd9d46qtftu68ki',  # Or path to database file if using sqlite3.
        'USER': 'oithnhwamizxka',  # Not used with sqlite3.
        'PASSWORD': '6OrH6cRnkAugNL44gxypx_SpdQ',  # Not used with sqlite3.
        'HOST': 'ec2-23-21-187-45.compute-1.amazonaws.com',  # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '5432',  # Set to empty string for default. Not used with sqlite3.
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Mexico_City'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
MEDIA_URL = '/media/'

STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(RUTA_PROYECTO, 'images')
MEDIA_ROOT_MOVIL = os.path.join(RUTA_PROYECTO, 'static')

#STATIC_ROOT = ''
#La ruta absoluta al directorio donde collectstatic recogerá archivos estáticos para la implementación.


# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

#STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.CachedStaticFilesStorage'

# various locations.
STATICFILES_DIRS = (
    # I have the static folder inside my app and not inside the project
    os.path.join(RUTA_PROYECTO, 'static'),
)


TEMPLATE_DIRS = (
    'templates',
)

import socket
a = socket.gethostbyname(socket.gethostname())
if str(a) == '127.0.1.1':
    facebook_key = "1539556102987271"#Local
    facebook_secret = "330159cf0d1b6a8a98c0e35c564365a8"#Local
else:
    facebook_secret = "330159cf0d1b6a8a98c0e35c564365a8"#Produccion
    facebook_key = "1539556102987271"#Produccion

print facebook_key

#-----------------Autentificacion con red socil--------------
SOCIAL_AUTH_FACEBOOK_KEY = "1476656729277209"#Produccion
#SOCIAL_AUTH_FACEBOOK_KEY = "1539556102987271"#Local
SOCIAL_AUTH_FACEBOOK_SECRET = "5c1f80475bcef95cef58f523ab14df27"#Produccion
#SOCIAL_AUTH_FACEBOOK_SECRET = "330159cf0d1b6a8a98c0e35c564365a8"#Local
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

AUTHENTICATION_BACKENDS = (
   'social.backends.facebook.FacebookOAuth2',
   #'social.backends.google.GoogleOAuth2',
   #'social.backends.twitter.TwitterOAuth',
   'django.contrib.auth.backends.ModelBackend',
)
# URLs
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/validar-acceso/'#Cuando me logee bien
SOCIAL_AUTH_LOGIN_URL = '/login/'#Cuando aya algun error

SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.user.create_user',
    'inicio.views.acceso_user',  # <--- set the path to the function
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details'
)
#-----------------Autentificacion con red socil--------------

