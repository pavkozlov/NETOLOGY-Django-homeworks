from collections import Counter
from django.shortcuts import render_to_response

counter_show = Counter()
counter_click = Counter()


def index(request):
    from_landing = request.GET.get('from-landing')
    counter_click[from_landing] += 1
    return render_to_response('index.html')


def landing(request):
    test = request.GET.get('ab-test-arg')
    counter_show[test] += 1
    if test == 'test':
        return render_to_response('landing_alternate.html')
    elif test == 'original':
        return render_to_response('landing.html')


def stats(request):
    test_conversion = 0 if counter_show['test'] == 0 else round(counter_click['test'] / counter_show['test'], 2)
    original_conversion = 0 if counter_show['original'] == 0 else round(counter_click['original'] / counter_show['original'], 2)

    return render_to_response('stats.html', context={
        'test_conversion': test_conversion,
        'original_conversion': original_conversion,
    })
