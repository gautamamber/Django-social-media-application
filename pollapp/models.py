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


class Subscriber(models.Model):
	email = models.EmailField()

	def __str__(self):
		return str(self.email)

	class Meta:
		verbose_name = 'Subscriber'
		verbose_name_plural = 'Subscriber'


class SendNewsLetter(models.Model):
	title = models.CharField(max_length = 200, blank = True, verbose_name = "News Title")
	text = models.TextField()
	links = models.URLField()

	def __str__(self):
		return str(self.title)

	class Meta:
		verbose_name_plural = "News Letter"
		verbose_name = "News Letter"

class State(models.Model):
	state = models.CharField(max_length = 100)

	def __str__(self):
		return str(self.state)

	class Meta:
		verbose_name = "State"
		verbose_name_plural = "State"

class Party(models.Model):
	party = models.CharField(max_length = 100)

	def __str__(self):
		return str(self.party)

	class Meta:
		verbose_name = "Party"
		verbose_name_plural = "Party"


class ElectionUpdate(models.Model):
	state = models.ForeignKey(State, on_delete = models.CASCADE)
	party = models.ManyToManyField(Party, blank = True)
	total_no_of_seats = models.IntegerField(blank = True)
	result = models.TextField(null = True)

	def __str__(self):
		return str(self.state)

	class Meta:
		verbose_name = "Election Update"
		verbose_name_plural = "Election Update"	



