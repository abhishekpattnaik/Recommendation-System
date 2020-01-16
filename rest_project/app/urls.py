from app import views
from django.conf.urls import url
from django.urls import path

urlpatterns = [
    path('urlDetails',views.url_detail.as_view()),
    path('testDetails',views.test_detail.as_view()),
    path('like_url',views.like_url.as_view()),
    # 'like_url'
]