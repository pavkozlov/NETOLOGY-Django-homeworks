from django.core.management.base import BaseCommand
from project_app.models import Station, Route
import csv
import os
from django.conf import settings


class Command(BaseCommand):

    def handle(self, *args, **options):
        with open(os.path.join(settings.BASE_DIR, 'moscow_bus_stations.csv'), encoding='cp1251') as f:
            fields = f.readline().strip().split(';')
            fields = list(map(lambda x: x.strip('"'), fields[0:len(fields) - 1]))
            csv_reader = csv.DictReader(f, fieldnames=fields, delimiter=';')

            for row in csv_reader:
                if Station.objects.filter(name=row['StationName']).count == 0:
                    station = Station()
                    station.latitude = row['Latitude_WGS84']
                    station.longtitude = row['Longitude_WGS84']
                    station.name = row['StationName']
                    station.save()
                    for route in row['RouteNumbers'].split(';'):
                        r = Route.objects.filter(name=route)
                        if r.count() > 0:
                            res = r.first()
                        else:
                            res = Route.objects.create(name=route)
                        station.routes.add(res)
                    station.save()
