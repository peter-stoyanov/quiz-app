from django.contrib import admin

# Register your models here.
from quizes.models import Quiz


class QuizAdmin(admin.ModelAdmin):
    pass


admin.site.register(Quiz, QuizAdmin)
