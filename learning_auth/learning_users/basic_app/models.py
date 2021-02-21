from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):
    # We will add additional information to the following model in this current model we are creating (UserProfileInfo)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Additional
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username
