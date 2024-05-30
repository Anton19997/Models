
from django.contrib import admin
from .models import Author, Book, Borrower, Borrow, Article, Comment, LikeDislike

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_available')
    search_fields = ('title',)
    filter_horizontal = ('authors',)

admin.site.register(Author)
admin.site.register(Book, BookAdmin)
admin.site.register(Borrower)
admin.site.register(Borrow)
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(LikeDislike)

