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
SECRET_KEY = 'some secret key'

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


    def run(parent_folder, port = 8000):
        Server.system(f'cd {parent_folder}; python manage.py runserver {port}')
    

    def create(method, name, content = ''):
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

from .models import Model1, Model2

# Register your models here.

class Default(args):
    model = Model2
    extra = 3


class Default2(args):
    fieldsets = [
        (None,               {'fields': ['text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [Default]
    list_display = ('text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['text']

admin.site.register(Model1, Defautlt2)
admin.site.register(Model2)
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
class Model1(models.Model):
    text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    
    def __str__(self):
        return self.text
    

    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    
    
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Model2(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    
    def __str__(self):
        return self.choice_text
""")
                    if n == 'tests.py':
                        file.write(
f"""
import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Model2
# Create your tests here.

class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        "
        The detail view of a question with a pub_date in the future
        returns a 404 not found.
        "
        future_question = create_question(text='Future question.', days=5)
        url = reverse('{i}:detail', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        "
        The detail view of a question with a pub_date in the past
        displays the question's text.
        "
        past_question = create_question(text='Past Question.', days=-5)
        url = reverse('{i}:detail', args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.text)


def create_question(text, days):
    "
    Create a question with the given `text` and published the
    given number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    "
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(text=text, pub_date=time)


class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        "
        If no questions exist, an appropriate message is displayed.
        "
        response = self.client.get(reverse('{i}:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_past_question(self):
        "
        Questions with a pub_date in the past are displayed on the
        index page.
        "
        question = create_question(text="Past question.", days=-30)
        response = self.client.get(reverse('{i}:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            [question],
        )

    def test_future_question(self):
        "
        Questions with a pub_date in the future aren't displayed on
        the index page.
        "
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse('{i}:index'))
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_future_question_and_past_question(self):
        "
        Even if both past and future questions exist, only past questions
        are displayed.
        "
        question = create_question(text="Past question.", days=-30)
        create_question(text="Future question.", days=30)
        response = self.client.get(reverse('{i}:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            [question],
        )

    def test_two_past_questions(self):
        "
        The questions index page may display multiple questions.
        "
        question1 = create_question(text="Past question 1.", days=-30)
        question2 = create_question(text="Past question 2.", days=-5)
        response = self.client.get(reverse('{i}:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            [question2, question1],
        )


class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        "
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        "
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        "
        was_published_recently() returns False for questions whose pub_date
        is older than 1 day.
        "
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        "
        was_published_recently() returns True for questions whose pub_date
        is within the last day.
        "
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)
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

from .models import Model1, Model2

# Create your views here.
class IndexView(generic.ListView):
    template_name = '%s/index.html'
    context_object_name = 'latest_question_list'


    def get_queryset(self):
        "
        Return the last five published questions (not including those set to be
        published in the future).
        "
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = '%s/detail.html'
    def get_queryset(self):
        "
        Excludes any questions that aren't published yet.
        "
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = '%s/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, '%s/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('%s:results', args=(question.id,)))
""" % (i, i, i, i, i))
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