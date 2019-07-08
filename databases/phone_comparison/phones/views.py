from django.shortcuts import render
from .models import Asus, Apple, Xiaomi, Samsung, Phone


def show_catalog(request):
    template = 'catalog.html'
    result = list()

    phones = Phone.objects.all()
    for i in phones:
        res = {
            'brand': i.brand,
            'camera': i.camera,
            'ram': i.ram,
            'price': i.price,
            'display': i.display,
            'bluetooth': i.bluetooth,
        }

        if i.brand == 'Apple':
            res['kit'] = Apple.objects.get(id=1).kit
        if i.brand == 'Samsung':
            res['fastcharge'] = i.samsung.first().fastcharge
        if i.brand == 'Asus':
            res['nfs'] = Asus.objects.get(id=1).nfs
        if i.brand == 'Xiaomi':
            res['hyroscope'] = Xiaomi.objects.get(id=1).hyroscope

        result.append(res)
    context = {
        'phones': result
    }
    return render(
        request,
        template,
        context
    )
