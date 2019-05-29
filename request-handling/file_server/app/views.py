from datetime import datetime
from django.conf import settings
import os
from django.shortcuts import render


def file_list(request, year=None, month=None, day=None):
    template_name = 'index.html'
    path = settings.FILES_PATH
    files = os.listdir(path)

    result = dict()
    result['files'] = list()

    for file in files:
        statinfo = os.stat(path + '/' + file)
        file_ctime = datetime.fromtimestamp(statinfo[9]).strftime('%d %B %Y г. %H:%M')
        file_mtime = datetime.fromtimestamp(statinfo[8]).strftime('%d %B %Y г. %H:%M')

        context = {
            'files': [
                {'name': file,
                 'ctime': file_ctime,
                 'mtime': file_mtime}
            ],
        }
        result['files'] += context['files']

    if year and month and day:
        my_date = datetime(year, month, day).strftime('%d %B %Y г. %H:%M')
        my_date = datetime.strptime(my_date, '%d %B %Y г. %H:%M')
        res = list()
        for file in result['files']:
            file['ctime'] = datetime.strptime(file['ctime'], '%d %B %Y г. %H:%M')
            file['mtime']= datetime.strptime(file['mtime'], '%d %B %Y г. %H:%M')
            if file['ctime'].date() == my_date.date():
                res.append(file)
        return render(request, template_name, context={'files': res, 'date': my_date.date()})

    return render(request, template_name, context={'files': result['files']})


def file_content(request, name):
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    path = settings.FILES_PATH
    files = os.listdir(path)
    for file in files:
        if name == file:
            with open(path + '/' + file) as f:
                content = f.read()
            return render(request, 'file_content.html', context={'file_name': file, 'file_content': content})
