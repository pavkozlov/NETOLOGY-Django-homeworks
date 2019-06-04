from datetime import datetime
from django.conf import settings
import os
from django.shortcuts import render


def file_list(request, year=None, month=None, day=None):
    template_name = 'index.html'
    path = settings.FILES_PATH
    logs = os.listdir(path)

    result = dict()
    result['files'] = list()

    for log in logs:
        statinfo = os.stat(path + '/' + log)
        log_ctime = datetime.fromtimestamp(statinfo[9])
        log_mtime = datetime.fromtimestamp(statinfo[8])

        formated_log = {
            'name': log,
            'ctime': log_ctime,
            'mtime': log_mtime}

        if all([year, month, day]):
            result['date'] = datetime(year, month, day)
            if formated_log['ctime'].date() == result['date'].date():
                result['files'].append(formated_log)
        else:
            result['files'].append(formated_log)

    if result.get('date'):
        context = {'files': result['files'], 'date': result['date']}
    else:
        context = {'files': result['files']}

    return render(request, template_name, context=context)


def file_content(request, name):
    path = settings.FILES_PATH
    logs = os.listdir(path)
    for log in logs:
        if name == log:
            with open(path + '/' + log) as f:
                content = f.read()
            return render(request, 'file_content.html', context={'file_name': log, 'file_content': content})
