import datetime
from django.db import models
from autoslug import AutoSlugField
from app_author.models import Profile
from markdownx.models import MarkdownxField


class Category(models.Model):
    """
    Category Model
    """
    id = models.AutoField(
        primary_key=True
    )

    category_title = models.CharField(
        max_length=200,
        verbose_name=u'Category Name',
        blank=False,
        null=False
    )

    slug = AutoSlugField(
        populate_from='category_title',
        unique=True
    )

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return str(self.category_title)

    @models.permalink
    def get_absolute_url(self):
        """
        Call Category Slug
        """
        return 'app_forum:category'


class Forum(models.Model):
    """
    Thread Model
    """
    forum_author = models.ForeignKey(
        Profile,
        related_name='user_forums',
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )

    forum_title = models.CharField(
        max_length=225,
        verbose_name=u'Title',
        blank=False,
        null=False
    )

    forum_category = models.ForeignKey(
        'Category',
        verbose_name=u'Category',
    )

    forum_content = MarkdownxField(
        verbose_name=u'Content (Use Markdown)',
    )

    is_created = models.DateTimeField(
        default=datetime.datetime.now,
        null=True,
        blank=True
    )

    is_modified = models.DateTimeField(
        default=datetime.datetime.now,
        null=True,
        blank=True
    )

    is_hot = models.BooleanField(
        default=False
    )

    is_closed = models.BooleanField(
        default=False
    )

    def __str__(self):
        return str(self.forum_title)

    def latest_comment_author(self):
        return self.forum_comments.latest('is_created').comment_author

    def latest_comment_date(self):
        return self.forum_comments.latest('is_created').is_created

    @models.permalink
    def get_absolute_url(self):
        """
        Call Forum ID
        """
        return 'app_forum:forum'


class Comment(models.Model):
    """
    Comment Model
    """
    forum = models.ForeignKey(
        'Forum',
        related_name='forum_comments'
    )

    comment_author = models.ForeignKey(
        Profile,
        related_name='user_comments',
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )

    comment_content = MarkdownxField(
        verbose_name=u'Markdown',
    )

    is_created = models.DateTimeField(
        auto_now_add=True,
    )

    is_modified = models.DateTimeField(
        auto_now=True,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.comment_content
