from django.contrib import admin
from .models import Post, Comment, Body


class BodyInline(admin.TabularInline):
    model = Body
    extra = 1


@admin.register(Post)
class Postadmin(admin.ModelAdmin):
    inlines = (BodyInline,)
    list_display = ('id', 'title', 'created_date')
    search_fields = ('title', )
    list_filter = ('category', 'tags')
    date_hierarchy = 'created_date'
    filter_horizontal = ('tags', )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'parent_comment', 'top_level_comment_id', 'created_date')
    search_fields = ('author__first_name', 'author__last_name', 'author__username', 'post__title', 'top_level_comment_id',)
    date_hierarchy = 'created_date'



