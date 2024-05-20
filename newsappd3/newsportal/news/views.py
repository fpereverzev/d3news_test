from django.shortcuts import render, get_object_or_404
from .models import Article


def news_list(request):
    articles = Article.objects.all().order_by('-published_date')
    return render(request, 'news_list.html', {'articles': articles})


def news_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'news_detail.html', {'article': article})
