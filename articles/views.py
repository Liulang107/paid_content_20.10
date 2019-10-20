from django.shortcuts import render
from .models import Article, Profile


def show_articles(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }

    return render(
        request,
        'articles.html',
        context
    )


def show_article(request, id):
    article = Article.objects.get(pk=id)
    context = {}
    context['title'] = article.title
    context['image'] = article.image

    if request.user.is_authenticated:
        user_subs = Profile.objects.get(user_id=request.user).subscription
    else:
        user_subs = False

    if article.paid_content and user_subs == False:
        context['text'] = 'Для того, чтобы читать данную статью необходимо подписаться на журнал!'
    else:
        context['text'] = article.text

    return render(
        request,
        'article.html',
        context
    )
