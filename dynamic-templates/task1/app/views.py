from django.shortcuts import render
import csv


def inflation_view(request):
    template_name = 'inflation.html'
    result = list()
    with open('inflation_russia.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            result.append(row[0].split(';'))
    res = list()
    for item in result:
        item = list(filter(lambda x: x != '', item))
        while len(item) < 13:
            item.append('-')
        res.append(item)
    result = res

    context = {
        'rows': result
    }

    return render(request, template_name, context=context)
