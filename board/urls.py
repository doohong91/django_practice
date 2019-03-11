from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('new/', views.new_article, name='new_article'),
    path('create/', views.create_article, name='create_article'),
    path('<int:article_id>/', views.article_detail, name='article_detail'),
    path('<int:article_id>/edit/', views.edit_article, name='edit_article'),
    path('<int:article_id>/update/', views.update_article, name='update_article'),
    path('<int:article_id>/delete/', views.delete_article, name='delete_article'),
]