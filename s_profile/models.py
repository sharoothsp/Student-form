from django.db import models

# Create your models here.
class Sprofile(models.Model):
    First_name = models.TextField()
    Last_name = models.TextField()
    Reg_No = models.TextField()
    Phone_number = models.IntegerField(null=True)
