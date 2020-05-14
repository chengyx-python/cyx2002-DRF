from django.db import models

# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(max_length=18)
    password = models.CharField(max_length=18,blank=True,null=True)
    phone = models.CharField(max_length=11)

    class Meta:
        db_table = "ba_user"
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return  self.username