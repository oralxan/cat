from django.db import models

class Post (models.Model):
    title=models.CharField(
        max_length=256,
        verbose_name='title'
        )
    sub_title=models.CharField(
        max_length=128,
        verbose_name='subtile',
        blank=True,
        null=True
        )
    description = models.TextField(
        verbose_name='descripison',
        blank=True,
        null=True
        )
    class Meta:
        verbose_name='post',
        verbose_name_plural='posty'