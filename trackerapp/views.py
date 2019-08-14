from django.shortcuts import render, render_to_response
from .models import Category, Expense, ExpenseForm, CategoryForm

def budget(request):
    expense_form = ExpenseForm()
    category_form = CategoryForm()
    edited_expense_id = None

    if request.method == 'POST':
        if 'expense-submit' in request.POST:
            edited_expense_id = request.POST['edited_expense_id']
            if edited_expense_id:
                expense_form = ExpenseForm(request.POST, instance=Expense.objects.get(id=edited_expense_id))
            else:
                expense_form = ExpenseForm(request.POST)

            if expense_form.is_valid():
                expense_form.save()
            expense_form = ExpenseForm()

        elif 'edit-expense' in request.POST:
            edited_expense_id = request.POST['expense-id']
            expense_form = ExpenseForm(instance=Expense.objects.get(id=edited_expense_id))

        elif 'delete-expense' in request.POST:
            expense = Expense.objects.get(id=request.POST['expense-id'])
            expense.delete()
        
        elif 'category-submit' in request.POST:
            category_form = CategoryForm(request.POST)
            if category_form.is_valid():
                category_form.save()  
            category_form = CategoryForm()  
        
        elif 'delete-category' in request.POST:
            category = Category.objects.filter(id=request.POST['category-id'])
            if category.exists():
                category = category.get()    
                category.delete()

    context  = {
        'categories': Category.objects.all(), 
        'expenses': Expense.objects.all(),
        'expense_form': expense_form,
        'edited_expense_id': edited_expense_id,
        'category_form': category_form
    }
    return render_to_response('budget.html', context)
