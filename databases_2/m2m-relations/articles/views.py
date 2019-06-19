from django.shortcuts import render
from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'

    articles = Article.objects.all().prefetch_related('articlescope_set').order_by('-published_at')

    context = {
        'object_list': articles
    }

    return render(request, template, context)
