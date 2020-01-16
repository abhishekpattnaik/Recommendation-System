from django.db import models

class url_details(models.Model):
	url = models.CharField(max_length=200)
	title = models.CharField(max_length=200)
	uid = models.CharField(max_length=200, primary_key=True)
	def __str__(self):
		return self.title


class app_user(models.Model):
	username = models.CharField(max_length=20, primary_key=True)
	liked_urls = models.ManyToManyField(url_details)
	def __str__(self):
		return str(self.username)

class recommended_article(models.Model):
	user = models.CharField(max_length=20, primary_key=True)
	liked_urls = models.ManyToManyField(url_details)
	# user = models.OneToOneField(app_user, on_delete=models.CASCADE)
	def __str__(self):
		return self.user


class super_user(models.Model):
	super_user_name = models.CharField(max_length=20, primary_key=True)
	user_urls = models.ManyToManyField(recommended_article)
	def __str_(self):
		return self.super_user_name
