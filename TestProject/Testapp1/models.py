from django.db import models
class articleModels(models.Model):
	author = models.CharField(max_length=200)
	claps = models.CharField(max_length=200)
	heading = models.CharField(max_length=200)
	articleType = models.CharField(max_length=200)
	description = models.TextField()
	articleUrl = models.CharField(max_length=200)
	def __str__(self):
		return self.author