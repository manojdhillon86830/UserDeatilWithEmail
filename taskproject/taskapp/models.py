from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class Content(models.Model):
    name=models.CharField(max_length=100)
    Email=models.EmailField()
    phone =models.IntegerField(null=False, blank=False, unique=True)
    Date_of_Birth=models.DateField()