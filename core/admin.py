from django.contrib import admin
from core.models import Expense

class ExpenseAdmin(admin.ModelAdmin):
    list_display = ['owner', 'item', 'cost', 'category']

admin.site.register(Expense, ExpenseAdmin)
