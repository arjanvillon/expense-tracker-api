import datetime
from django.db import models
from .choices import TRANSACTION_CATEGORIES


# Create your models here.
class Transaction(models.Model):
    """ Model for transactions e.g. Expense, Debt, Income """

    wallet = models.ForeignKey("users.Wallet", on_delete=models.CASCADE, related_name="transactions")
    category = models.CharField(max_length=10, choices=TRANSACTION_CATEGORIES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(default=datetime.date.today)
    note = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f'{self.wallet.name} transacted {self.amount} as {self.category}'    
