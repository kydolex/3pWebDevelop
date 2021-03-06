from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	title = models.CharField("タイトル", max_length=200)
	content = models.TextField("本文")
	created = models.DateTimeField("作成日", default=timezone.now)

	def __str__(self):
		return self.title

class Infomation_Post(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	title = models.CharField("タイトル", max_length=200)
	content = models.TextField("本文")
	created = models.DateTimeField("作成日", default=timezone.now)

	def __str__(self):
		return self.title

class Sample_Post(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	title = models.CharField("タイトル", max_length=200)
	content = models.TextField("本文")
	created = models.DateTimeField("作成日", default=timezone.now)

	def __str__(self):
		return self.title


class List_Post(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	title = models.CharField("タイトル", max_length=200)
	content = models.TextField("本文")
	image = models.ImageField(upload_to='images', verbose_name='イメージ画像', null=True, blank=True)
	created = models.DateTimeField("作成日", default=timezone.now)

	def __str__(self):
		return self.title



