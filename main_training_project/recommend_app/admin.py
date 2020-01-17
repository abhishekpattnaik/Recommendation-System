from django.contrib import admin
from recommend_app.models import UrlDetails, RecommendedArticle, AppUser, SuperUser
# Register your models here.
admin.site.register(UrlDetails)
admin.site.register(AppUser)
admin.site.register(SuperUser)
admin.site.register(RecommendedArticle)