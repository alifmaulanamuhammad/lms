#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import environ
from exc import execute_from_command_line(sys.argv)

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SMS.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) 


if __name__ == '__main__':
    # OS environment variables take precedence over variables from .env
    environ.Env.read_env()
    main()
