from django.db import models
from django.utils.html import format_html
from django.contrib.auth.models import User


#CATEGORY MODEL

class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category/')
    add_date = models.DateTimeField(auto_now_add=True, null=True)


    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def image_tag(self):
        return format_html('<img src="/media/{}" style="width:40px; height:40px; border-radius:50%;"  />'.format(self.image))

    def __str__(self):
        return self.title
#POST MODEL

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    url = models.CharField(max_length=100)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post/')
    likes = models.ManyToManyField(User, blank=True, related_name='likes')
    dislikes = models.ManyToManyField(User, blank=True, related_name='dislikes')

    def __str__(self):
        return self.title


class PostComment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    comments = models.CharField(max_length=500)
    posted_at = models.DateTimeField(auto_now_add=True)


    @property
    def imageURL(self):
        try:
            url = self.profile_image.url
        except:
            url = ''
        return url
