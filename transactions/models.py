from django.db import models

from groups.models import Person

# Create your models here.
class Transaction(models.Model):

    class Meta:
        verbose_name = "Transaction"
        verbose_name_plural = "Transactions"

    def __str__(self):
        pass

    name = models.TextField(default='')
    amount = models.FloatField()
    member = models.ForeignKey(Person, related_name="transaction_set")