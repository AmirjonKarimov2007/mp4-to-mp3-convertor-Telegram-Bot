from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(verbose_name='Fullname', max_length=100)
    username = models.CharField(verbose_name='Username', max_length=100, null=True)
    telegram_id = models.BigIntegerField(verbose_name='Telegram_id', unique=True, default=1)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.full_name


# async def create_table_users(self):
#     sql = """
#     CREATE TABLE IF NOT EXISTS Users (
#     id SERIAL PRIMARY KEY,
#     full_name VARCHAR(255) NOT NULL,
#     username varchar(255) NULL,
#     telegram_id BIGINT NOT NULL UNIQUE
#     );
#     """
#     await self.execute(sql, execute=True)
