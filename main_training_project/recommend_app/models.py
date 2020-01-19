from django.db import models

class UrlDetails(models.Model):
	'''
	This model will instantiate all the urls details 
	''' 
	url = models.CharField(max_length=200)
	title = models.CharField(max_length=200)
	uid = models.CharField(max_length=200, primary_key=True)
	def __str__(self):
		return self.title


class AppUser(models.Model):
	''' 
	This model will instantiate all sub user models fields 
	'''
	username = models.CharField(max_length=20)
	liked_urls = models.ManyToManyField(UrlDetails)
	def __str__(self):
		return str(self.username)

class RecommendedArticle(models.Model):
	''' 
	This model will instantiate all models fields for the user recommendations  
	'''
	user = models.CharField(max_length=20)
	liked_urls = models.ManyToManyField(UrlDetails)
	# user = models.OneToOneField(app_user, on_delete=models.CASCADE)
	def __str__(self):
		return self.user


class SuperUser(models.Model):
	''' 
	This model will instantiate all superuser models fields 
	'''
	super_user_name = models.CharField(max_length=20)
	user_urls = models.ManyToManyField(RecommendedArticle)
	def __str_(self):
		return self.super_user_name
