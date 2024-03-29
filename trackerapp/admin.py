from django.contrib import admin
from .models import Expense, Category


class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date', 'amount', 'notes', 'category')

admin.site.register(Expense, ExpenseAdmin)
admin.site.register(Category, admin.ModelAdmin)
