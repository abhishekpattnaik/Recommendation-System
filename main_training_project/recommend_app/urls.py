from recommend_app import views
from django.conf.urls import url
from django.urls import path

urlpatterns = [
    path('urlDetails',views.url_view.as_view()),
    path('recommend_app',views.app_user_view.as_view()),
    path('superuser',views.super_user_view.as_view()),
]