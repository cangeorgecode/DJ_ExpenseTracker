from django.db import models

catories = {
    'meal': 'meal',
    'stationary': 'stationary',
    'other': 'other'
}

class Expense(models.Model):
    date_created = models.DateField(auto_created=True)
    item = models.CharField(max_length=100)
    cost = models.FloatField()
    category = models.CharField(max_length=20, choices=catories)
    owner = models.IntegerField(blank=False)

    def __str__(self):
        return (f"{self.date_created, self.owner, self.item, self.cost, self.category}")
