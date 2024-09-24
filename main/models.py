from django.db import models
from django.contrib.auth.models import User
import uuid

class KambingEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # tambahkan baris ini
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    time = models.DateField(auto_now_add=True)
    description = models.TextField()
    

    @property
    def is_kambing_pricy(self):
        return self.price > 20000000
    
class monster(models.Model):
    name = models.CharField(max_length=199)
    email= models.EmailField()
    age = models.IntegerField()
    is_happy = models.BooleanField()
    muncul =models.DateField()