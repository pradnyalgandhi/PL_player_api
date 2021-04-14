from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(verbose_name="Email")

    def __str__(self):
        return f"{self.user}"

@receiver(post_save, sender=User)
def update_user_profile(sender,instance,created, **kwars):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

