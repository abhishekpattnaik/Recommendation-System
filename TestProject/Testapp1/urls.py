from django.urls import path
from Testapp1.views import articleDetail
urlpatterns = [
    path('articleDetails',articleDetail.as_view()),
]