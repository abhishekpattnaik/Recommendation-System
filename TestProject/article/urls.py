from django.urls import path
from article.views import ArticleView
app_name = "articles"
urlpatterns = [
    path('articles/', ArticleView.as_view()),
]