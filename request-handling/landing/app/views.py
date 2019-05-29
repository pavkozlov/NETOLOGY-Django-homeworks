from collections import Counter

from django.shortcuts import render_to_response

# Для отладки механизма ab-тестирования используйте эти счетчики
# в качестве хранилища количества показов и количества переходов.
# но помните, что в реальных проектах так не стоит делать
# так как при перезапуске приложения они обнулятся
counter_show = Counter()
counter_click = Counter()


def index(request):
    from_landing = request.GET.get('from-landing')
    if from_landing == 'test':
        counter_click['test'] += 1
    elif from_landing == 'original':
        counter_click['original'] += 1
    return render_to_response('index.html')


def landing(request):
    test = request.GET.get('ab-test-arg')
    if test == 'test':
        counter_show['test'] += 1
        return render_to_response('landing_alternate.html')
    elif test == 'original':
        counter_show['original'] += 1
        return render_to_response('landing.html')


def stats(request):
    try:
        test_conversion = round(counter_click['test'] / counter_show['test'], 2)
    except ZeroDivisionError:
        test_conversion = 0
    try:
        original_conversion = round(counter_click['original'] / counter_show['original'], 2)
    except ZeroDivisionError:
        original_conversion = 0
    return render_to_response('stats.html', context={
        'test_conversion': test_conversion,
        'original_conversion': original_conversion,
    })
