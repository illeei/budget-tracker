from django.db import models
from django import forms 

from functools import partial 

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name

    @property
    def total(self):
        expenses = Expense.objects.filter(category=self).values_list('amount', flat=True)
        return sum(expenses)

class Expense(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    notes = models.CharField(max_length=100, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)     

    def __str__(self):
        return '{} - {} : {}'.format(self.name, self.amount, self.date)

    

DateInput = partial(forms.DateInput, {'class': 'datepicker form-control', 'placeholder': ''})
DateInput.show_datepicker = True

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('date', 'name', 'amount', 'notes', 'category')
        widget = {
            'date': DateInput()
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)