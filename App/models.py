from django.db import models

class TradeHub(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='img/')

    def __str__(self):
        return self.name