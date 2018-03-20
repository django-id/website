from django.utils.text import slugify


def get_unique_slug(instance, field: str) -> str:
    attribute = getattr(instance, field)
    slug = slugify(attribute)
    unique_slug = slug
    num = 1
    queryset = instance.__class__.objects.filter(slug=unique_slug)
    while queryset.exists():
        unique_slug = '{slug}-{counter}'.format(slug=slug, counter=num)
        num += 1
    return unique_slug