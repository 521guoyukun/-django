from django.db import models
from django.contrib.auth.models import User  # 如果医生与内置用户模型关联，可取消注释此行


class Doctor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    title = models.CharField(max_length=50, blank=True)
    specialization = models.CharField(max_length=100)
    experience_years = models.IntegerField()
    hospital_affiliation = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)

    # 如果医生与内置用户模型关联
    # user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


from django.db import models

# Create your models here.
