from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Wallet(models.Model):
    """ The model where money is stored """

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="wallets")
    name = models.CharField(max_length=20)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.owner.username