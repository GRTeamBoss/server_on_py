#!usr/bin/env python3
#-*- encoding: utf-8 -*-


class File:


    def get_content(path):
        with open(f'{path}', 'r', encoding='utf-8') as file:
            read = file.read().split('\n')
            read = [f'{val}: {read[val]}' for val in range(0, len(read))]
            read = '\n'.join(read)
        return read


    def set_content(path, number,  content):
        with open(f'{path}', 'w+', encoding='utf-8') as file:
            read = file.read().split('\n')
            for val in range(0, len(read)):
                if val == number:
                    read[val] = content
            read = '\n'.join(read)
            file.write(read)
        return 0


    def add_content(path, number, content):
        with open(f'{path}', 'a', encoding='utf-8') as file:
            read = file.read().split('\n')
            for val in range(0, len(read)):
                if val == number:
                    read[val] += content
            read = '\n'.join(read)
            file.write(read)
        return 0