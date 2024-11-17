from django.db import models

class User(models.Model):
    name = models.CharField(verbose_name='Fullname', max_length=100)
    username = models.CharField(verbose_name='Username', max_length=100, null=True)
    user_id = models.BigIntegerField(verbose_name='Telegram_id', unique=True, default=1)

    def __str__(self):
        return self.name

