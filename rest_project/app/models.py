from django.db import models

# Create your models here.
class Friend(models.Model):
	name = models.CharField(max_length=100)

class Belonging(models.Model):
	name = models.CharField(max_length=200)

class Borrowed(models.Model):
	what = models.ForeignKey(Belonging, on_delete=models.CASCADE)
	to_who = models.ForeignKey(Friend, on_delete=models.CASCADE)
	when = models.DateTimeField(auto_now_add=True)
	returned = models.DateTimeField(null=True, blank=True)


class Url_Details(models.Model):
	url = models.CharField(max_length=200)
	title = models.CharField(max_length=200)
	uid = models.CharField(max_length=200)
	def __str__(self):
		return self.title


class test_model(models.Model):
	url = models.CharField(max_length=200)
	title = models.CharField(max_length=200)
	uid = models.CharField(max_length=200)
	like = models.BooleanField(default=False)
	def __str__(self):
		return self.title

class url_rating(models.Model):
	url_info = models.ForeignKey(Url_Details, on_delete=models.CASCADE)
	liked = models.BooleanField(default=False)