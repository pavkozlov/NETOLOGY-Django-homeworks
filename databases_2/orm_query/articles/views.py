from django.views.generic import ListView
from django.shortcuts import render

from .models import Article


def articles_list(request):
    template_name = 'articles/news.html'
    articles = Article.objects.all().select_related('author', 'genre').only('author__name', 'author__phone',
                                                                            'genre__name').order_by('-published_at')
    context = {
        'object_list': articles
    }

    return render(request, template_name, context)
