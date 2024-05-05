from django.shortcuts import render, redirect
from core.models import Expense
from core.forms import AddExpenseForm
from django.contrib import messages

def index(request):
    return render(request, 'core/index.html', {})

def dashboard(request):
    return render(request, 'core/dashboard.html', {})

def expense(request):
    if request.user.is_authenticated:
        form = AddExpenseForm()
        current_user_id = request.user.id
        expenses = Expense.objects.filter(owner=current_user_id)
        if request.method == "POST":
            form = AddExpenseForm(request.POST)
            if form.is_valid():
                expense_form = form.save(commit=False)
                expense_form.owner = current_user_id
                expense_form = form.save()
                messages.success(request, 'Expense has been added')
                return redirect('expense')
            else:
                messages.success(request, 'There was an error')
        return render(request, 'core/expense.html', {'form': form, 'expenses': expenses})
    else:
        messages.success(request, 'You must be logged in to add expenses')
        return redirect('index')