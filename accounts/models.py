from django.db import models
from django.contrib.auth.models import User


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
#


# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
#     name = models.CharField(max_length=255, null=True, blank=True)
#     email = models.EmailField(max_length=355, unique=True, null=True, blank=True)
#     username = models.CharField(max_length=255, null=True, blank=True)
#     location = models.CharField(max_length=55, null=True, blank=True)
#     profile_image = models.ImageField(null=True, blank=True, upload_to='profiles/')
#     created = models.DateTimeField(auto_now_add=True)
#
#
#     def __str__(self):
#         return self.user.username
#
#     class Meta:
#         ordering = ['-created']

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    location = models.CharField(max_length=55, null=True, blank=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to='images/')
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.user.username} Profile'
