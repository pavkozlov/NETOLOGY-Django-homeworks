from django.shortcuts import render
from .models import Phone


def show_catalog(request):
    sort_by = request.GET.get('sort_by')

    template = 'catalog.html'

    if sort_by == 'name':
        phones = Phone.objects.all().order_by('name')
    elif sort_by == 'low_price':
        phones = Phone.objects.all().order_by('price')
    elif sort_by == 'price':
        phones = reversed(Phone.objects.all().order_by('price'))
    else:
        phones = Phone.objects.all()

    result = list()

    for i in phones:
        res = {
            'id': i.id,
            'name': i.name,
            'price': i.price,
            'image': i.image,
            'release_date': i.release_date,
            'lte_exists': i.lte_exists,
            'slug': i.slug
        }
        result.append(res)

    context = {
        'phones': result
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {
        'id': phone.id,
        'name': phone.name,
        'price': phone.price,
        'image': phone.image,
        'release_date': phone.release_date,
        'lte_exists': phone.lte_exists,
        'slug': phone.slug
    }
    return render(request, template, context)
