from django.shortcuts import render, get_object_or_404
from .models import article, category
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView, UpdateView, DeleteView)


@login_required
def home(request):
    context = {
        'articles': article.objects.all(),
        'categories': category.objects.all(),
        'title': 'Home'
    }
    return render(request, 'article/home.html', context)


class ArticleListView(ListView):
    model = article
    template_name = 'article/home.html'
    context_object_name = 'articles'
    ordering = ['-date_posted']
    paginate_by = 7


class ArticleDetailView(DetailView):
    model = article
    template_name = 'article/article_detail.html'
    context_object_name = 'article'


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = article
    fields = ['title', 'description', 'content', 'category']
    template_name = 'article/article_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = article
    fields = ['title', 'description', 'content', 'category']
    template_name = 'article/article_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        article = self.get_object()
        if self.request.user == article.author:
            return True
        return False


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = article
    template_name = 'article/article_confirm_delete.html'
    context_object_name = 'article'
    success_url = '/'

    def test_func(self):
        article = self.get_object()
        if self.request.user == article.author:
            return True
        return False


class UserArticlesListView(ListView):
    model = article
    template_name = 'article/article_user.html'
    context_object_name = 'articles'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return article.objects.filter(author=user).order_by('-date_posted')


class AllArticleListView(ListView):
    model = article
    template_name = 'article/article_all.html'
    context_object_name = 'articles'
    ordering = ['-date_posted']
    paginate_by = 7


def AllArticles(request):
    context = {
        'articles': article.objects.all(),
        'categories': category.objects.all(),
        'title': 'All Articles'
    }
    return render(request, 'article/article_all.html', context)


def UserArticles(request):
    return render(request, 'article/article_user.html')
