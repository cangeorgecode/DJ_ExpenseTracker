from django.db import models

catories = {
    'meal': 'meal',
    'stationary': 'stationary',
    'other': 'other'
}

status = {
    'pending': 'pending',
    'approved': 'approved',
    'rejected': 'rejected',
}

class Expense(models.Model):
    date_created = models.DateField(auto_created=True, null=True)
    item = models.CharField(max_length=100)
    cost = models.FloatField()
    category = models.CharField(max_length=20, choices=catories)
    owner = models.IntegerField(blank=False)
    receipt = models.ImageField(upload_to='images/', null=True, blank=True)
    status = models.CharField(max_length=20, choices=status, default='pending')

    def __str__(self):
        return (f"{self.date_created, self.owner, self.item, self.cost, self.category}")
