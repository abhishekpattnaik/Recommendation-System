from recommend_app import views,swagger
from django.conf.urls import url
from django.urls import path
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='My API')

urlpatterns = [
    path('recommend_app',views.AppUserView.as_view()),
    # path('recommend_app',views.AppUserView.as_view()),
    path('superuser',views.SuperUserView.as_view()),
    path('login',views.Login.as_view()),
    path('register',views.RegisterUser.as_view()),
    path('schema/',schema_view),
]