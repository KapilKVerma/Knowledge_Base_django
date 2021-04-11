from django.urls import path
from . import views
from .views import (ArticleListView, ArticleDetailView,
                    ArticleCreateView, ArticleUpdateView,
                    ArticleDeleteView, UserArticlesListView,
                    AllArticleListView)


urlpatterns = [
    path('', ArticleListView.as_view(),
         name='article-home'),
    path('article/<int:pk>/', ArticleDetailView.as_view(),
         name='article-details'),
    path('article/new/', ArticleCreateView.as_view(), name='article-create'),
    path('article/<int:pk>/update/',
         ArticleUpdateView.as_view(), name='article-update'),
    path('article/<int:pk>/delete/',
         ArticleDeleteView.as_view(), name='article-delete'),
    path('<str:username>/articles/', UserArticlesListView.as_view(),
         name='article-user'),
    path('articles/', AllArticleListView.as_view(), name='all-articles')
]
