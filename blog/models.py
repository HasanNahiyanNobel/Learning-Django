from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)  # on_delete causes the post to be deleted when we delete the user.

	def __str__(self):
		return self.title
