import os


def generate(project):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Q12306.server.server.settings')
    # os.environ.setdefault('RUN_MAIN', 'true')
    import django
    django.setup()
    from Q12306.server.core.utils import generate_project
    generate_project(project)
