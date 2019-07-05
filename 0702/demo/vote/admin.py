from django.contrib import admin

# Register your models here.

from .models import Question, Choice


class ChoiceAdmin(admin.StackedInline):
    model = Choice
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceAdmin, ]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
