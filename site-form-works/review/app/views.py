from django.shortcuts import redirect, render, get_object_or_404
from .models import Product, Review
from .forms import ReviewForm


def product_list_view(request):
    template = 'app/product_list.html'
    products = Product.objects.all()

    context = {
        'product_list': products,
    }

    return render(request, template, context)


def product_view(request, pk):
    template = 'app/product_detail.html'
    product = get_object_or_404(Product, id=pk)
    reviews = product.review_set.all()

    if not request.session.get('reviewed_products'):
        request.session['reviewed_products'] = list()

    if request.method == 'POST':
        form = ReviewForm(request, pk, request.POST)
        if form.is_valid():
            Review.objects.create(text=form.cleaned_data['text'], product=Product.objects.get(id=pk))
            request.session['reviewed_products'].append(pk)
            return redirect('product_detail', pk=pk)

    elif request.method == 'GET':
        form = ReviewForm(request, pk)

    context = {
        'form': form,
        'product': product,
        'reviews': reviews
    }

    return render(request, template, context)
