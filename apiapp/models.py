from django.db import models

# Create your models here.
class MoringaMerch(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20)

    def __str__(self):
        return self.name