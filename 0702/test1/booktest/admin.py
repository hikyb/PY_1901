from django.contrib import admin
from .models import BookInfo, HeroInfo

# Register your models here.


class BookInfoAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date')
    list_filter = ('pub_date',)
    search_fields = ('title',)


class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'content', 'book')
    list_filter = ('book',)
    search_fields = ('name', 'content')
    list_per_page = 2


admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo, HeroInfoAdmin)

