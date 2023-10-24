from django.db import models


class Post(models.Model):
    title = models.TextField()
    slug = models.SlugField()
    date_added = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    intro = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['-date_added']


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    text = models.CharField(max_length=1000)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_added']
