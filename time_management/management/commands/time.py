from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Manage adjust selected time implementation to current time'

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('--request-time', nargs='+', type=int)
        # Named (optional) arguments
        parser.add_argument(
            '--delete',
            action='store_true',
            dest='delete',
            default=False,
            help='Delete poll instead of closing it',
        )

    def handle(self, *args, **options):
        for request_time in options['request_time']:
            self.stdout.write(self.style.SUCCESS('Successfully request_time "%s"' % request_time))
