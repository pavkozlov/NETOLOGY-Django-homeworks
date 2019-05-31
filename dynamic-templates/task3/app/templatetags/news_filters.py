from django import template
import datetime
import re

register = template.Library()


@register.filter
def format_date(value):
    value = datetime.datetime.fromtimestamp(value)
    now = datetime.datetime.now()
    if (now - value) < datetime.timedelta(hours=0, minutes=10, seconds=0):
        return 'Только что'
    elif (now - value) < datetime.timedelta(hours=24, minutes=0, seconds=0):
        return f'{(now - value).seconds // 3600} часов назад'
    elif (now - value) > datetime.timedelta(hours=24, minutes=0, seconds=0):
        return value.strftime('%Y %B %d')


# необходимо добавить фильтр для поля `score`


@register.filter
def format_num_comments(value):
    value = int(value)
    if value == 0:
        return "Оставьте комментарий"
    elif 0 < value < 50:
        return value
    elif value > 50:
        return '50+'


@register.filter
def format_scope(scope):
    scope = int(scope)
    if scope < -5:
        return 'Всё плохо'
    elif -5 < scope < 5:
        return 'Нейтрально'
    elif scope > 5:
        return 'Хорошо'


@register.filter
def format_selftext(value, count):
    value.replace('\n', ' ')
    value = value.split(' ')

    value1 = value[:count]
    value2 = value[len(value) - count:]

    result = ' '.join(value1) + '...' + ' '.join(value2)
    if result != '...':
        return result
    else:
        return ''
