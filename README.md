
<h1 align="center">
  <br>
  <a href="http://www.django.id"><img src="http://i.pi.gy/j33Ng.png" alt="Django Indonesia" width="200"></a>
  <br>
  Django Indonesia
  <br>
</h1>

<h4 align="center">Clean and simple forum app made for Django-id Community. Built on top of <a href="https://www.djangoproject.com/" target="_blank">Django</a> and <a href="">Markdown</a>.</h4>

<p align="center">
  <a href="https://badge.fury.io/js/electron-markdownify">
    <img src="https://img.shields.io/pypi/pyversions/Django.svg"
         alt="Gitter">
  </a>
  <a href="https://gitter.im/amitmerchant1990/electron-markdownify"><img src="https://img.shields.io/pypi/status/Django.svg"></a>
  <a href="https://saythanks.io/to/amitmerchant1990">
      <img src="https://img.shields.io/packagist/l/doctrine/orm.svg">
  </a>
  <a href="https://www.paypal.me/AmitMerchant">
    <img src="https://img.shields.io/website-up-down-green-red/http/shields.io.svg?label=django.id">
  </a>
</p>
<br>

![screenshot](http://i.pi.gy/JDDdP.png)

## Key Features

* LivePreview Editor - Make changes, See changes
  - Instantly see what your Markdown documents look like in HTML as you create them.
* Built on top of Django Framework and Python 3.X
* GitHub Flavored Markdown  
* Syntax highlighting
* Use [SASS](http://sass-lang.com/)
* Use [Bulma](https://bulma.io/), modern front-end framework
* [Pygments](http://pygments.org/) Support
* Simple and clean UI/UX
* ~~No-bullshit~~ No-nonsense, get the job done.
* Made with love and passion


## How To Use

To clone and run this application, you'll need [Git](https://git-scm.com), [virtualenv](http://www.pythonforbeginners.com/basics/how-to-use-python-virtualenv) and [Python](https://www.python.org/) installed on your computer. I assume you already setup the django environment on your machine, if not yet, then Google is your friend. From your command line:

```bash
# Create virtual environment using virtualenv
$ virtualenv -p python3 envname

# Go into virtual environment folder
$ cd envname

# Activate virtualenv
$ source bin/activate

# Clone this repository
$ git clone https://github.com/django-id/website.git django_id

# Go into the repository
$ cd django_id

# Install requirements
$ pip install -r requirements.txt

# Migrate the databse
$ python manage.py makemigrations && python manage.py migrate

# Run the app
$ python manage.py runserver
```

Note:<br>
If those commands is not working, please open issue with detailed error messages.<br>
Do not forget to rename from `settings_test.py` to `settings.py`


## Download

You can [download](https://github.com/django-id/website/archive/master.zip) latest relase version of Django ID also.

## Credits

This software uses code from several open source packages.

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [MarkdownX](https://github.com/neutronX/django-markdownx)
- [Pygments](http://pygments.org/)
- [Bulma](https://bulma.io/)
- And soo many other great and amazing open source projects!

## To-Do List

- Add emojis
- Create user mention/tagging feature
- Create notification system
- Create proper paginations
- Fixing its responsiveness
- Polishing its UI/UX
- ...

## Changelog

- v0.2 : Add user stats (Total posts and total threads) on profile page
- v0.1 : Intial release

#### License

MIT

---

> [Facebook](https://www.facebook.com/groups/DjangoID/) &nbsp;&middot;&nbsp;
> [Github](https://github.com/django-id/) &nbsp;&middot;&nbsp;
> [Slack](http://django-id.herokuapp.com/)
