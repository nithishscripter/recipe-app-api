"""Custom management command to wait for the Data Base to be available."""

from django.core.management.base import BaseCommand
from django.db.utils import OperationalError

from psycopg2 import OperationalError as Psycopg2OpError

import time


class Command(BaseCommand):
    """Django command to wait for db."""

    def handle(self, *args, **options):
        """Entrypoint for Command."""

        db_up = False
        self.stdout.write("Preparing Database...")

        while not db_up:
            try:
                self.check(databases=['default'])
                db_up = True
            except(OperationalError, Psycopg2OpError):
                self.stdout.write("Database is unavailable, re-trying...")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database AVAILABLE!"))
