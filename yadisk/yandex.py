import yadisk
from django.shortcuts import redirect

from input import token


y = yadisk.YaDisk(token=token)
name_dir = "/Mohnatii"
list_staff = ['Свет', 'Звук', 'Видео', 'Декорация', 'Реквизит', 'Грим', 'Костюм']


def yandexUpload(file, path_to, path_from):
    if y.check_token():
        if not y.is_dir(name_dir):
            y.mkdir(name_dir)
            print('Папка "Mohnatii" создана')
        else:
            print("vse zaebis")
            if not y.is_dir(f'{name_dir}/{path_to}'):
                y.mkdir(f'{name_dir}/{path_to}')
                y.upload(f'{path_from}{file}', f'{name_dir}/{path_to}/{file}', overwrite=True)
                print(f'Папка {path_to} создана')
            else:
                y.upload(f'{path_from}{file}', f'{name_dir}/{path_to}/{file}', overwrite=True)
                print('snova zaebis')

yandexUpload('favicon.ico', 'zalupa', path_from='../')

def yandexDownload(file, path_to, path_from):
    if y.is_file(f'{name_dir}/{path_to}/{file}'):
        y.download(f'{name_dir}/{path_to}/{file}', f'../main/static/temp/{name_dir}{path_to}{file}')
        return (f'../main/static/temp/{name_dir}{path_to}{file}')

