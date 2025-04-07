#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

# ЭТО СТАНДАРТНЫЙ (основной) ФАЙЛ ДЖАНГИ, ТУТ Я ОБЪЯСНЮ ВСЕ ОСТАЛЬНЫЕ ФАЙЛЫ/ПАПКИ
# ПАПКА templates ВКЛЮЧАЕТ В СЕБЯ САМ САЙТ НА HTML (СГЕНЕРИРОВАНЫ В ИИ), ФАЙЛЫ В ПАПКЕ project ЯВЛЯЮТСЯ СТАНДАРТНЫМИ ДЛЯ ДЖАНГИ (КАК И ЭТОТ) (но были введены правки
# ФАЙЛЫ В ПАПКЕ users УЖЕ НАПИСАНЫ ОТ СЕБЯ
# ДЛЯ ЗАПУСКА СЕРВЕРА ОБЯЗАТЕЛЬНО ПРОПИСАТЬ:
# pip install -r project/requirements.txt
# (для создания этого файла (НЕ ПРОПИСЫВАТЬ): django-admin startproject apps,
# ПИСАТЬ ЭТО python project/manage.py makemigrations
# И ЭТО python project/manage.py migrate
# А ЭТО ЗАПУСК СЕРВЕРА python project/manage.py runserver 127.0.0.1:5432 (project/manage.py) - ПУТЬ ДО ФАЙЛА ЭТОГО, (127.0.0.1:5432) - АЙПИ ЭТО ЛОКАЛХОСТ ПОРТ СТАНДАРТНЫЙ ОТ ДЖАНГИ (вроде)