from django.contrib import admin
from app.models import user_liked, Url_Details, test_model, url_rating, super_user
# Register your models here.
admin.site.register(Url_Details)
admin.site.register(test_model)
admin.site.register(url_rating)
admin.site.register(user_liked)
admin.site.register(super_user)