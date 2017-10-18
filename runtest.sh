#!/usr/bin/env bash
coverage run --source='.' manage.py test --settings=djangoid.settings_test -v 1 && coverage html -i
