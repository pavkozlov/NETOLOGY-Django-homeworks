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
    return value.strftime('%Y %B %d')


# необходимо добавить фильтр для поля `score`


@register.filter
def format_num_comments(value):
    value = int(value)
    if value == 0:
        return "Оставьте комментарий"
    elif 0 < value < 50:
        return value
    return '50+'


@register.filter
def format_scope(scope):
    scope = int(scope)
    if scope < -5:
        return 'Всё плохо'
    elif -5 < scope < 5:
        return 'Нейтрально'
    return 'Хорошо'


@register.filter
def format_selftext(value, count):
    temp_value = value.replace('\n', ' ')
    temp_value = temp_value.split(' ')

    if len(temp_value) <= count * 2:
        return value

    value1 = temp_value[:count]
    value2 = temp_value[len(temp_value) - count:]

    result = ' '.join(value1) + '...' + ' '.join(value2)

    return result


print(format_selftext(value='one two three four', count=2))
