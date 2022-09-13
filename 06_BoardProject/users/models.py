from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    # primary_key 를 User 의 pk 로 설정하여 통합적으로 관리
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    nickname = models.CharField(max_length=128)
    position = models.CharField(max_length=128)
    subjects = models.CharField(max_length=128)
    image = models.ImageField(upload_to='profile/', default='default.png')


@receiver(post_save, sender=User)   # User 모델이 post_save 이벤트를 발생할 경우
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
