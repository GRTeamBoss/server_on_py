#!usr/bin/env python3
#-*- encoding: utf-8 -*-

# frameworks and libraries
import os, platform


class Server:


    def docs():
        info = \
"""
Documentation:
folders tree:
---------
project/
    project/
        __pycache__/
            __init__.cpython-39.pyc
            settings.cpython-39.pyc
        __init__.py
        asgi.py
        settings.py
        urls.py
        wsgi.py
    app/
        migrations/
            __init__.py
        __init__.py
        admin.py
        apps.py
        models.py
        tests.py
        views.py
    manage.py
---------
default content when you create project and app with help Django:
---------
project-folder/manage.py:
#!/usr/bin/env python
"Django's command-line utility for administrative tasks."
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'default.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
---------
project-folder/project/__init__.py:
*empty*
---------
project-folder/project/asgi.py:
"
ASGI config for default project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'default.settings')

application = get_asgi_application()
---------
project-folder/project/settings.py:
"
Django settings for default project.

Generated by 'django-admin startproject' using Django 3.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')@z-ehhwab03@2ulcgxkf!d_+1zk4i7-5i!#ys8a$jaajo$r=n'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
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

ROOT_URLCONF = 'default.urls'

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

WSGI_APPLICATION = 'default.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
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
---------
project-folder/project/urls.py:
"default URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
---------
project-folder/project/wsgi.py:
"
WSGI config for default project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'default.settings')

application = get_wsgi_application()
---------
project-folder/project/widget/migrations/__init__.py
*empty*
---------
project-folder/project/widget/__init__.py:
*empty*
---------
project-folder/project/widget/admin.py:
from django.contrib import admin

# Register your models here.

---------
project-folder/project/widget/apps.py:
from django.apps import AppConfig


class WidgetConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'widget'

---------
project-folder/project/widget/models.py:
from django.db import models

# Create your models here.

---------
project-folder/project/widget/tests.py:
from django.test import TestCase

# Create your tests here.

---------
project-folder/project/widget/views.py:
from django.shortcuts import render

# Create your views here.

---------
"""

        return info


    def system(arg):
        os.system(arg)


    def get(path):
        with open(f'{path}', 'r', encoding='utf-8') as file:
            read = file.read().split('\n')
            read = [f'{val}: {read[val]}' for val in range(0, len(read))]
            read = '\n'.join(read)
        return read


    def set(path, number,  content = ''):
        with open(f'{path}', 'w+', encoding='utf-8') as file:
            read = file.read().split('\n')
            for val in range(0, len(read)):
                if val == number:
                    read[val] = content
            read = '\n'.join(read)
            file.write(read)
        return 0


    def add(path, number, content = ''):
        with open(f'{path}', 'a', encoding='utf-8') as file:
            read = file.read().split('\n')
            for val in range(0, len(read)):
                if val == number:
                    read[val] += content
            read = '\n'.join(read)
            file.write(read)
        return 0
    
    def install(method, arg):
        """
        1 method:
        install(1, Django)
        2 method:
        install(2, pip install Django)
        """
        if method == 1:
            Server.system(f'pip install {arg}')
        if method == 2:
            Server.system(f'{arg}')
        return 0


    def start(arg = 'mysite'):
        Server.system(f'django-admin startproject {arg}')


    def app(name = 'app'):
        Server.system(f'python manage.py startapp {name}')


    def migrate(parent_folder):
        Server.system(f'cd {parent_folder}; python manage.py migrate')


    def run(port = 8000):
        Server.system(f'python manage.py runserver {port}')
    

    def create(method, name = 'default', content = ''):
        """
        1 method:
        create folder:
        create(folder*, foldername)
        2 method:
        create file:
        create(file*, filename.txt, content)
        -----
        method is required
        """
        osName = platform.system()
        if osName == 'Linux' or osName == 'Darwin':
            if method == 'folder':
                Server.system(f'mkdir {name}')
            if method == 'file':
                Server.system(f'echo {content} > {name}')
        if osName == 'Windows':
            if method == 'folder':
                Server.system(f'mkdir {name}')
            if method == 'file':
                Server.system(f'echo {content} > {name}')


    def edit(parent_folder = 'default', project = 'default', app = ['widget',]):
        PROJECT_LINKS = ['asgi.py', 'settings.py', 'urls.py', 'wsgi.py']
        APP_LINKS = ['admin.py', 'apps.py', 'models.py', 'tests.py', 'views.py']
        for i in PROJECT_LINKS:
            with open(f'./{parent_folder}/{project}/{i}', 'w+', encoding='utf-8') as file:
                read = file.read().split('\n')
                if i == 'asgi.py':
                    pass
                if i == 'settings.py':
                    pass
                if i == 'urls.py':
                    pass
                if i == 'wsgi.py':
                    pass
        for i in app:
            for n in APP_LINKS:
                with open(f'./{parent_folder}/{i}/{n}', 'w+', encoding='utf-8') as file:
                    read = file.read().split('\n')
                    if n == 'admin.py':
                        pass
                    if n == 'apps.py':
                        pass
                    if n == 'models.py':
                        pass
                    if n == 'tests.py':
                        pass
                    if n == 'views.py':
                        pass