from django.forms import ModelForm
from .models import Article
from django import forms
import django_filters

class ArticleForm(ModelForm):

    data = django_filters.DateFilter(lookup_expr='gt', widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Article
        fields = ['name', 'ARtext', 'author', 'data']