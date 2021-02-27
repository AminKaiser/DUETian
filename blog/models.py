from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
# Create your models here.

class Post(models.Model):
	CATEGORY = (
			('General Post', 'General Post'),
			('Job Post', 'Job Post'),
			('Special Post', 'Special Post'),
			)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	category = models.CharField(max_length=200, null=True, choices=CATEGORY)
	title = models.CharField(max_length=100)
	content = models.TextField()
	picture = models.ImageField(upload_to='post/content_pictures', null=True, blank=True)
	date_posted = models.DateTimeField(default=timezone.now)


	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		super(Post, self).save(*args, **kwargs)

		img = Image.open(self.picture.path)

		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.picture.path)

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})


class Comment(models.Model):
	post = models.ForeignKey(Post, related_name='comments',on_delete=models.CASCADE)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	text = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.post.pk})

	def __str__(self):
		return self.text
