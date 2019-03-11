from django.shortcuts import render

# Create your views here.
def article_list(request):
    return render(request, 'board/index.html')


def article_detail(request, article_id):
    pass


def new_article(request):
    pass


def create_article(request):
    pass


def edit_article(request, article_id):
    pass


def update_article(request, article_id):
    pass


def delete_article(request, article_id):
    pass