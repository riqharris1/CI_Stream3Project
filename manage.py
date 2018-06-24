#!/usr/bin/env python
Stream3Project/env/bin/python manage.py runserver
import os
import sys

if __name__ == "__main__":
	#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.base")
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.staging")
    #os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.dev")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
