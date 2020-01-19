from recommend_app import views
from django.conf.urls import url
from django.urls import path

urlpatterns = [
    path('recommend_app',views.AppUserView.as_view()),
    path('superuser',views.SuperUserView.as_view()),
]