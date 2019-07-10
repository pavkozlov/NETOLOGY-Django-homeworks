import time
import random

from django.shortcuts import render
from django.http import JsonResponse
from django.core.cache import cache

from .models import City
from .forms import SearchTicket


def ticket_page_view(request):
    template = 'app/ticket_page.html'

    context = {
        'form': SearchTicket()
    }

    return render(request, template, context)


def cities_lookup(request):
    """Ajax request предлагающий города для автоподстановки, возвращает JSON"""
    query = cache.get_or_set('cities', City.objects.all()).filter(name__startswith=request.GET['term'])
    results = [city.name for city in query]

    return JsonResponse(results, safe=False)
