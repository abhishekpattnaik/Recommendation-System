from django.urls import path
from app.views import index,register

urlpatterns = [
    path('', index.as_view(), name='index'),
    path('register', register, name='register'),
]
