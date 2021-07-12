#!usr/bin/env python3
#-*- encoding: utf-8 -*-

# frameworks and libraries
from edit import Edit
from docs import Docs
from manipulate import File
from terminal import Terminal


class Server:


    def docs():
        return Docs.info()


    def get(path):
        return File.get_content(path)


    def set(path, number,  content = ''):
        return File.set_content(path, number, content)


    def add(path, number, content = ''):
        return File.add_content(path, number, content)
        
    
    def install(method, arg):
        return Terminal.apt(method, arg)


    def start(arg = 'mysite'):
        return Terminal.startproject(arg)


    def app(name = 'app'):
        return Terminal.startapp(name)


    def migrate(parent_folder, method = 'migrate'):
        return Terminal.migration(parent_folder, method)


    def run(parent_folder, port = 8000):
        return Terminal.runserver(parent_folder, port)
    

    def create(method, name, content = ''):
        return Terminal.create(method, name, content)


    def edit(parent_folder = 'default', project = 'default', app = ['widget',]):
        return Edit.edit(parent_folder, project, app)