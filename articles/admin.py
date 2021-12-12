from django.contrib import admin
from .models import article, comments


class CommentInline(admin.StackedInline):  # new
    model = comments


class ArticleAdmin(admin.ModelAdmin):  # new
    inlines = [
        CommentInline,
    ]


admin.site.register(article, ArticleAdmin)  # new
admin.site.register(comments)
# Register your models here.
