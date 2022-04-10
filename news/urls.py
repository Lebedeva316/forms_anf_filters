from django.urls import path
from .views import ArticleList, ArticleDetail, Search, Add_news, Edit_news, Delete_news, ArticleDetailView

urlpatterns = [
   path('news_list/', ArticleList.as_view()),
   path('<int:pk>', ArticleDetailView.as_view(), name='news_detail'),
   path('search/', Search.as_view()),
   path('add/', Add_news.as_view(), name='news_create'),
   path('<int:pk>/edit/', Edit_news.as_view(), name='news_edit'),
   path('<int:pk>/delete/', Delete_news.as_view(), name='news_delete'),
]
