from django.db import models
class mediumModels(models.Model):
	author = models.CharField(max_length=200)
	claps = models.CharField(max_length=200)
	heading = models.CharField(max_length=200)