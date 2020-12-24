from django.contrib import admin

# Register your models here.
from budget.models import Expense, ExpenseType


class ExpenseAdmin(admin.ModelAdmin):
    pass


admin.site.register(Expense, ExpenseAdmin)


class ExpenseTypeAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name = 'Expense TType'
        verbose_name_plural = 'Expense TTypes '


admin.site.register(ExpenseType, ExpenseTypeAdmin)
