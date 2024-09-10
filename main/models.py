from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    

    @property
    def is_kambing_pricy(self):
        return self.price > 20000000