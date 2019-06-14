from django.shortcuts import render
import csv
from django.conf import settings


def inflation_view(request):
    template_name = 'inflation.html'
    with open(settings.CSV_FILE) as f:
        fieldnames = f.readline().strip().split(';')
        reader = csv.DictReader(f, fieldnames=fieldnames, delimiter=';')
        result = list(dict(i) for i in reader)

    context = {
        'rows': result,
        'fieldnames': fieldnames
    }

    return render(request, template_name, context=context)
