from django.contrib import admin
from app_forum.models import Category, Comment, Forum


class ForumAdmin(admin.ModelAdmin):
    """
    Post in Admin
    """
    model = Forum
    list_display = [
        'forum_title',
        'forum_author',
        'is_closed',
        'is_hot'
    ]

    list_filter = (
        'forum_author',
        'is_created',
        'is_hot',
    )


class CategoryAdmin(admin.ModelAdmin):
    """
    Thread Category Admin
    """
    model = Category
    list_display = [
        'id',
        'category_title'
    ]


class CommentAdmin(admin.ModelAdmin):
    """
    Comment Admin
    """
    model = Comment
    list_display = [
        'forum',
        'comment_author',
    ]


admin.site.register(Forum, ForumAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
