#!/usr/bin/env bash
coverage run --source='.' manage.py test --settings=djangoid.settings_test -v 2 && coverage html -i
