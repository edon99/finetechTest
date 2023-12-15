
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.



class Receipt(models.Model):
    store_name = models.CharField(max_length=100)
    date = models.DateField()
    item_list = models.CharField(max_length=100)
    total = models.DecimalField(decimal_places=2,max_digits=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
  


