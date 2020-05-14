from django.db import models

# Create your models here.
class Employee(models.Model):
    gender_choices = (
        (0, "male"),
        (1, "female"),
        (2, "other")
    )
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64, blank=True, null=True)
    gender = models.SmallIntegerField(choices=gender_choices, default=1)
    phone = models.CharField(max_length=11, null=True, blank=True)
    pic = models.ImageField(upload_to="pic", default="pic/1.jpg")

    class Meta:
        db_table = "bz_emp"
        verbose_name = "员工"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username