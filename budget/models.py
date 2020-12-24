from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class ExpenseType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return 'Type: ' + self.name


class Expense(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.ForeignKey(ExpenseType, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Expense: ' + str(self.amount) + ' ( ' + self.type.name + ' )'
