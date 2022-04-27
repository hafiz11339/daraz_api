from django.db import models

# Create your models here.
class DarazData(models.Model):
    title = models.CharField(max_length=400)
    price = models.CharField(max_length=150)
    img = models.CharField(max_length=600)
    url = models.CharField(max_length=500)
    sku = models.CharField(max_length=200)
    name = models.CharField(max_length=10000)

    @property
    def get_price(self):
        return self.price.split('Rs. ')[1]