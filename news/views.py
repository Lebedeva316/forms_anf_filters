from django.shortcuts import render
from datetime import datetime

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Article
from .filters import ArticleFilter
from .forms import ArticleForm

class ArticleList(ListView):

    model = Article
    ordering = '-data'
    template_name = 'news.html'
    context_object_name = 'Articles'
    paginate_by = 10
    form_class=ArticleForm
    queryset = Article.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = None
        context['filter'] = ArticleFilter(self.request.GET, queryset=self.get_queryset())

        return context


    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)  # создаём новую форму, забиваем в неё данные из POST-запроса

        if form.is_valid():  # если пользователь ввёл всё правильно и нигде не ошибся, то сохраняем новый товар
            form.save()

        return super().get(request, *args, **kwargs)


class ArticleDetail(DetailView):

    model = Article
    template_name = 'Article.html'
    context_object_name = 'Article'

class Search(ListView):

    model = Article
    ordering = '-data'
    template_name = 'search.html'
    context_object_name = 'search'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = None
        context['filter'] = ArticleFilter(self.request.GET, queryset=self.get_queryset())
        return context

class ArticleDetailView(DetailView):

    context_object_name = 'Article'
    template_name = 'Article.html'
    queryset = Article.objects.all()

class Add_news(CreateView):

    form_class = ArticleForm
    template_name = 'Add_news.html'
    context_object_name = 'Article'


class Edit_news(UpdateView):

    form_class = ArticleForm
    template_name = 'Edit_news.html'
    context_object_name = 'Article'

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Article.objects.get(pk=id)

class Delete_news(DeleteView):

    template_name = 'Delete_news.html'
    success_url = '/news/news_list/'
    context_object_name = 'Article'
    queryset = Article.objects.all()


