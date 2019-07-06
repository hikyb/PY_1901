from django.contrib import admin
from .models import Question, Choice
# Register your models here.


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('desc', 'vote', 'question')
    list_per_page = 12
    list_filter = ('question',)
    search_fields = ('desc',)


class ChoiceInlines(admin.StackedInline):
    model = Choice
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInlines]
    list_display = ('desc', 'pub_date')
    search_fields = ('desc',)


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
