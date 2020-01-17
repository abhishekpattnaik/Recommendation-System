from recommend_app.views import MainUrlView
from rest_framework import routers

main_router = routers.DefaultRouter()
main_router.register('recommeded_app', MainUrlView, basename='recommeded_app_test')