from django.contrib import admin
from recommend_app.models import url_details, recommended_article, app_user, super_user
# Register your models here.
admin.site.register(url_details)
admin.site.register(app_user)
admin.site.register(super_user)
admin.site.register(recommended_article)