from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from budget.forms import ExpenseForm
from budget.models import Expense


@login_required
def create_expense(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense_instance = form.instance
            expense_instance.user = request.user
            form.save()
            return redirect('/budget/all')
    else:
        form = ExpenseForm()
    return render(request, 'create_expense.html', {'form': form})


@login_required
def all_expenses(request):
    expenses = Expense.objects.all().filter(user=request.user)
    return render(request, 'list_expenses.html', {'expenses': expenses})
