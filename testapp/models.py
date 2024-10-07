from django.db import models
from django.contrib.auth.models import User

class ExpenseModel(models.Model):
    date = models.DateField()
    category = models.CharField(max_length=250)
    description = models.TextField(max_length=1000)
    amount = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
   
    def __str__(self):
        return f'{self.user.username} - {self.category}: {self.amount} on {self.date}'
