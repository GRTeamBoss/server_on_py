#!usr/bin/env python3
#-*- encoding: utf-8 -*-

import os, platform

class Terminal:


    def apt(method, arg):
        """
        1 method:
        install(1, Django)
        2 method:
        install(2, pip install Django)
        """
        if method == 1:
            os.system(f'pip install {arg}')
        if method == 2:
            os.system(f'{arg}')
        return 0


    def startproject(arg = 'mysite'):
        os.system(f'django-admin startproject {arg}')


    def startapp(name = 'app'):
        os.system(f'python manage.py startapp {name}')


    def migration(parent_folder, method):
        if method == 'migrate':
            os.system(f'cd {parent_folder}; python manage.py {method}')
        if method == 'makemigration':
            os.system(f'cd {parent_folder}; python manage.py {method}')


    def runserver(parent_folder, port):
        os.system(f'cd {parent_folder}; python manage.py runserver {port}')
    

    def create(method, name, content):
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
                os.system(f'mkdir {name}')
            if method == 'file':
                os.system(f'echo {content} > {name}')
        if osName == 'Windows':
            if method == 'folder':
                os.system(f'mkdir {name}')
            if method == 'file':
                os.system(f'echo {content} > {name}')