from django.db import models

# Create your models here.
class BaseModel(models.Model):
    is_alive = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class Emp(BaseModel):
    name = models.CharField(max_length=12)
    age = models.SmallIntegerField()
    addr = models.CharField(max_length=123)
    salary = models.DecimalField(max_digits=7,decimal_places=2)

    class Meta:
        db_table = 'test_emp'
        verbose_name = '员工'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
