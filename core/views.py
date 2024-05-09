from django.shortcuts import render, redirect
from core.models import Expense
from core.forms import AddExpenseForm
from django.contrib import messages
from django.http import HttpResponse
import csv

def index(request):
    return render(request, 'core/index.html', {})

def dashboard(request):
    return render(request, 'core/dashboard.html', {})

def expense(request):
    if request.user.is_authenticated:
        current_user_id = request.user.id
        if request.user.is_superuser:
            expenses = Expense.objects.all()
            return render(request, 'core/expense.html', {'expenses': expenses,})
        else:
            expenses = Expense.objects.filter(owner=current_user_id)
            return render(request, 'core/expense.html', {'expenses': expenses,})
        # return render(request, 'core/expense.html', {'expenses': expenses,})
    else:
        messages.success(request, 'You must be logged in to add expenses')
        return redirect('index')
    
def approve(request, item_id):
    if request.user.is_superuser:
        expense_item = Expense.objects.get(id=item_id)
        form = AddExpenseForm(request.POST or None, instance=expense_item)
        form.fields['date_created'].disabled = True
        form.fields['item'].disabled = True
        form.fields['cost'].disabled = True
        form.fields['category'].disabled = True
        form.fields['receipt'].disabled = True
        if form.is_valid():
            form.save()
            return redirect('expense')
        return render(request, 'core/approve.html', {'form': form})
    if request.user.is_authenticated:
        expense_item = Expense.objects.get(id=item_id)
        form = AddExpenseForm(request.POST or None, request.FILES or None, instance=expense_item)
        if form.is_valid():
            form.instance.status = 'pending'
            form.save()
            return redirect('expense')
        return render(request, 'core/approve.html', {'form': form})
    
def submit(request):
    if request.user.is_authenticated:
        form = AddExpenseForm()
        if not request.user.is_superuser:
            form.fields['status'].disabled = True
            current_user_id = request.user.id
            if request.method == "POST":
                form = AddExpenseForm(request.POST, request.FILES)
                if form.is_valid():
                    expense_form = form.save(commit=False)
                    expense_form.owner = current_user_id
                    expense_form = form.save()
                    messages.success(request, 'Expense has been added')
                    return redirect('expense')
                else:
                    messages.success(request, 'There was an error')
        return render(request, 'core/submit.html', {'form': form})
    
def export_csv_record(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=expenses.csv'
    writer = csv.writer(response)
    expenses = Expense.objects.all()
    writer.writerow(['Date Created', 'Item', 'Cost', 'Category', 'Owner', 'Status'])
    for expense in expenses:
        writer.writerow([expense.date_created.strftime("%d-%b-%Y"), expense.item, expense.cost, expense.category, expense.owner, expense.status])
    return response