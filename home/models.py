from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class Post(models.Model):
    postId = models.AutoField(primary_key=True, )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.postId) + ' by ' + str(self.user)


class UserDetails(models.Model):
    username = models.OneToOneField(User,
                                    on_delete=models.CASCADE,
                                    primary_key=True)
    fname = models.CharField(max_length=50, blank=True)
    lname = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    rating = models.FloatField(null=True)
    institute = models.CharField(max_length=200, blank=True)
    experience = models.CharField(max_length=200, blank=True)
    location = models.CharField(max_length=500, blank=True)
    pPhoto = models.ImageField(upload_to="users/images",
                               default='users/images/default.png')
    status = models.IntegerField(null=True)
    phone = models.CharField(max_length=15, blank=True)
    links = models.CharField(max_length=200, blank=True)
    slug = models.CharField(max_length=500, default=username)

    def __str__(self):
        return str(self.username)
