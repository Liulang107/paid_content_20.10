from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    subscription = models.BooleanField(default=False, verbose_name='Подписка')


class Article(models.Model):
    title = models.CharField(max_length=120, verbose_name='Заголовок')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение')
    text = models.TextField(verbose_name='Текст')
    paid_content = models.BooleanField(verbose_name='Платный контент')

