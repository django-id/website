from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# CUSTOM FILE SIZE VALIDATOR


def validate_image(fieldfile_obj):
    """
    Limit image size upload
    """
    filesize = fieldfile_obj.file.size
    megabyte_limit = 0.5
    if filesize > megabyte_limit*1024*1024:
        raise ValidationError("Max file size is %sMB" % str(megabyte_limit))


class Profile(models.Model):
    """
    Author Model
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    profile_picture = models.ImageField(
        upload_to='images/%Y/%m/%d',
        validators=[validate_image],
        blank=True,
        null=True
    )

    profile_name = models.CharField(
        verbose_name='Name',
        null=True,
        blank=True,
        max_length=50
    )

    profile_email = models.EmailField(
        verbose_name='Email Address',
        null=True,
        blank=True
    )

    profile_location = models.CharField(
        verbose_name='Origin/City',
        null=True,
        blank=True,
        max_length=50
    )

    profile_github = models.URLField(
        verbose_name='Github URL',
        null=True,
        blank=True
    )

    slug = models.SlugField()

    is_created = models.DateTimeField(
        null=True,
        blank=True
    )

    is_moderator = models.BooleanField(
        default=False,
    )

    def __str__(self):
        return str(self.user)

    def save(self, **kwargs):
        if not self.slug:
            from djangoid.utils import get_unique_slug
            self.slug = get_unique_slug(instance=self, field='profile_name')
        super(Profile, self).save(**kwargs)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Automatically Create User when Login
    """
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """
    Automatically Create User when Login
    """
    instance.profile.save()
