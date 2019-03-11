from django.shortcuts import render, get_object_or_404
from .models import Article


# Create your views here.
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'board/list.html', {'articles': articles})


def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'board/detail.html', {'article': article})


def new_article(request):



def create_article(request):
    pass


def edit_article(request, article_id):
    pass


def update_article(request, article_id):
    pass


def delete_article(request, article_id):
    pass