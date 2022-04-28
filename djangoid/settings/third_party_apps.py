from .local import INSTALLED_APPS

INSTALLED_APPS = INSTALLED_APPS + [
    'taggit',
    'markdownx',
    'crispy_forms',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.github',
]
