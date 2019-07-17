from django.shortcuts import render
from .models import Route, Station


# Create your views here.

def stations_view(request):
    routes = Route.objects.all()

    data = dict()
    data['routes'] = routes

    if request.GET.get('route'):
        r = routes.filter(name=request.GET['route'])
        if r.count() > 0:
            route = r.first()
            x_res = list()
            y_res = list()
            for x in route.stations.all():
                x_res.append(x.latitude)
                y_res.append(x.longtitude)
            data['center'] = {
                'y': float(sum(x_res) / max(len(x_res), 1)),
                'x': float(sum(y_res) / max(len(y_res), 1)),
            }
            data['stations'] = route.stations.all()

    return render(request, 'stations.html', context=data)
