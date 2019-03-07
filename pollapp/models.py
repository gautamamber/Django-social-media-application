from django.db import models

# Create your models here.

from django.urls import reverse

# Create your models here.
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):
	author = models.ForeignKey('auth.User', on_delete = models.CASCADE)
	title = models.CharField(max_length= 100)
	text = models.TextField()
	image = models.ImageField(upload_to = 'New/%Y/%m/%d', blank = True)
	created_date = models.DateTimeField(default = timezone.now)
	published_date = models.DateTimeField(blank = True, null = True)
	likes = models.ManyToManyField('auth.User', related_name = "likes" , blank = True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title

	def total_likes(self):
		return self.likes.count()

	def get_absolute_url(self):
		return reverse("pollapp:details" , args = [self.id])

	class Meta:
		verbose_name = "Post"
		verbose_name_plural = "Post"

class Comment(models.Model):
	post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name = 'aa')
	user = models.ForeignKey(User , on_delete = models.CASCADE)
	# reply = models.ForeignKey('self', null = True, related_name = 'replies', blank = True, on_delete = models.CASCADE)
	content = models.TextField(max_length = 100)
	timestamp = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return '{}-{}'.format(self.post.title, str(self.user.username))

	class Meta:
		verbose_name = "Comment"
		verbose_name_plural = "Comment"

class News(models.Model):
	author = models.ForeignKey('auth.User', on_delete = models.CASCADE)
	title = models.CharField(max_length= 100)
	text = models.TextField()
	# simage = models.ImageField(upload_to = 'New/%Y/%m/%d', blank = True)
	created_date = models.DateTimeField(default = timezone.now)
	published_date = models.DateTimeField(blank = True, null = True)


	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("pollapp:details" , args = [self.id])

	class Meta:
		verbose_name = "News"
		verbose_name_plural = "News"



class Poll(models.Model):
	poll_between = models.CharField(max_length = 100, blank = True, null = True)
	first_poll = models.ImageField(upload_to = 'New/%Y/%m/%d', blank = True)
	second_poll = models.ImageField(upload_to = 'New/%Y/%m/%d', blank = True)
	first_poll_count = models.IntegerField(default = 0)
	second_poll_count = models.IntegerField(default = 0)

	class Meta:
		verbose_name_plural = "Poll"
		verbose_name = "Poll"

	def  __str__(self):
		return str(self.poll_between)

