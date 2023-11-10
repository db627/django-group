from django.core.management.base import BaseCommand
from myapp.factory import UserFactory, CourseFactory, ToDoFactory

class Command(BaseCommand):
    help = 'Seeds the database with User and Course data'

    def add_arguments(self, parser):
        parser.add_argument(
            '--users',
            type=int,
            help='Number of users to create'
        )

        parser.add_argument(
            '--courses',
            type=int,
            help='Number of courses to create'
        )
        parser.add_argument(
            '--todo',
            type=int,
            help='Number of days to create'
        )

    def handle(self, *args, **kwargs):
        num_users = kwargs['users'] or 100  # Default to 100 if not specified
        num_courses = kwargs['courses'] or 50  # Default to 50 if not specified
        num_todo = kwargs['todo'] or 10
        self.stdout.write('Seeding {} users...'.format(num_users))
        UserFactory.create_batch(num_users)

        self.stdout.write('Seeding {} courses...'.format(num_courses))
        CourseFactory.create_batch(num_courses)

        self.stdout.write('Seeding {} ToDo...'.format(num_courses))
        ToDoFactory.create_batch(num_todo)

        self.stdout.write(self.style.SUCCESS('Database seeding complete!'))
