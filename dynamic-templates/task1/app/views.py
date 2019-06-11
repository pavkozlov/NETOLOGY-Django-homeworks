from django.shortcuts import render
import csv
from django.conf import settings


def inflation_view(request):
    template_name = 'inflation.html'
    with open(settings.CSV_FILE) as f:
        fieldnames = ['year', 'jan', 'feb', 'march', 'apr', 'may', 'jun', 'july', 'aug', 'sept', 'oct', 'nov', 'dec', 'summ']
        reader = csv.DictReader(f, fieldnames=fieldnames, delimiter=';')
        result = list(dict(i) for i in reader)

    context = {
        'rows': result
    }

    return render(request, template_name, context=context)
