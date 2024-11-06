# app1/management/commands/runserver_app1.py
from django.core.management.commands.runserver import Command as RunserverCommand

class Command(RunserverCommand):
    def add_arguments(self, parser):
        super().add_arguments(parser)
        parser.add_argument('addrport', nargs='?', default='8001', help='Optional port number')