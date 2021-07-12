#!usr/bin/env python3
#-*- encoding: utf-8 -*-


class Edit:


    def edit(parent_folder, project, app):

        PROJECT_LINKS = ['asgi.py', 'settings.py', 'urls.py', 'wsgi.py']

        APP_LINKS = ['admin.py', 'apps.py', 'models.py', 'tests.py', 'views.py', 'urls.py']

        for i in PROJECT_LINKS:

            with open(f'./{parent_folder}/{project}/{i}', 'w+', encoding='utf-8') as file:
                if i == 'asgi.py':
                    file.write(
f"""
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', '{project}.settings')

application = get_asgi_application()
""")
                if i == 'settings.py':
                    read = file.read().split('\n')
                    log = []
                    for i in read:
                        log.append(i.find('SECRET_KEY'))
                    for i in log:
                        if i == 0:
                            key = read[log.index(i)]
                    file.write(
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
%s

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    %s
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = '%s.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR , 'templates'],
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

WSGI_APPLICATION = '%s.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydatabase',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'                    
""" % (key, ',\n'.join(f'{x}.apps.{x}Config,' for x in app), project, project))
                if i == 'urls.py':
                    file.write(
f"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("{app}/", include('{app}.urls'))
]
""")
                if i == 'wsgi.py':
                    file.write(
f"""
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', '{project}.settings')

application = get_wsgi_application()
""")
        for i in app:
            for n in APP_LINKS:
                with open(f'./{parent_folder}/{i}/{n}', 'w+', encoding='utf-8') as file:
                    if n == 'admin.py':
                        file.write(
"""
from django.contrib import admin

from .models import #[This is tables from DB which describe in models.py]

# Register your models here.

# Here you can describe tables which will be watch in /admin.html
""")
                    if n == 'apps.py':
                        file.write(
f"""
from django.apps import AppConfig


class {i}Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = '{i}'
""")
                    if n == 'models.py':
                        file.write(
"""
import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin

# Create your models here.


# class Example(models.Model):
#     text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
    
    
#     def __str__(self):
#         return self.text
""")
                    if n == 'tests.py':
                        file.write(
f"""
import datetime

from .models import #[This is table from DB which describe in models.py]
# Create your tests here.
""")
                    if n == 'views.py':
                        file.write(
"""
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import #[This is table from DB which describe in models.py]

# Create your views here.
class IndexView(generic.ListView):
    template_name = '%s/index.html'
    context_object_name = 'latest_question_list'
""" % i)
                    if n == 'urls.py':
                        file.write(
f"""
from django.urls import path

from . import views

app_name = '{i}'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
""")