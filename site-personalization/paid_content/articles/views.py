from django.shortcuts import render, redirect
from .models import Article, Profile


def show_articles(request):
    articles = Article.objects.all().only('name', 'id')
    return render(request, 'articles.html', context={'articles': articles})


def show_article(request, id):
    article = Article.objects.get(id=id)

    if article.premium:
        user = Profile.objects.get(user=request.user.id) if request.user.is_authenticated else None
        if not user or not user.is_subscribe:
            data = {'need_subscribe': True, 'name': article.name}
            return render(request, 'article.html', context=data)

    data = {
        'image': article.image,
        'text': article.text,
        'name': article.name
    }

    return render(request, 'article.html', context=data)


def subscribe(request):
    if request.method == 'POST' and request.user.is_authenticated:
        user = Profile.objects.get(user=request.user.id)
        user.is_subscribe = True
        user.save()
        return redirect('show_articles')

    is_auth = request.user.is_authenticated

    return render(request, 'subscribe.html', context={'is_auth': is_auth})
