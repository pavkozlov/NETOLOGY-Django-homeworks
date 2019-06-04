from django.shortcuts import render_to_response, redirect
from django.urls import reverse
import csv
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage
from urllib.parse import urlencode


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    file = settings.BUS_STATION_CSV
    order = ['ID', 'Name', 'Longitude_WGS84', 'Latitude_WGS84', 'Street', 'AdmArea', 'District', 'RouteNumbers',
             'StationName', 'Direction', 'Pavilion', 'OperatingOrgName', 'EntryState', 'global_id', 'geoData']
    with open(file, encoding='cp1251') as f:
        f.readline()
        reader = csv.DictReader(f, fieldnames=order)
        result = list(reader)

    paginator = Paginator(result, 10)
    page = request.GET.get('page')
    if page is None: page = 1

    try:
        res = paginator.page(page)
    except EmptyPage:
        res = paginator.page(paginator.num_pages)
        page = paginator.num_pages

    next_page = int(page) + 1
    prev_page = int(page) - 1 if page and int(page) > 1 else 1

    return render_to_response('index.html', context={
        'bus_stations': res,
        'current_page': page,
        'prev_page_url': 'bus_stations?' + urlencode({'page': prev_page}),
        'next_page_url': 'bus_stations?' + urlencode({'page': next_page}),
    })
