from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser

# Create your models here.
User = get_user_model()

# class User(AbstractUser):
#     friends = models.ManyToManyField("User", blank=True, related_name='user_friends')
#     groups = models.ManyToManyField('auth.Group', related_name='user_groups', blank=True)
#     user_permissions = models.ManyToManyField('auth.Permission', related_name='user_permissions_set', blank=True)


class Profile(models.Model):
    # these are the compulsory fields for this model
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    # these will be filled in later by the user
    bio = models.TextField(blank=True)
    profileimg = models.ImageField(upload_to='profile_images', default='blank-profile-picture.png')
    location = models.CharField(max_length=100, blank=True)
    #friends = models.ManyToManyField(User, related_name='friend')

    def __str__(self):
        return self.user.username
    
# class Friend_Request(models.Model):
#     from_user = models.ForeignKey(User, related_name='from_user', on_delete=models.CASCADE)
#     to_user = models.ForeignKey(User, related_name='to_user', on_delete=models.CASCADE)

