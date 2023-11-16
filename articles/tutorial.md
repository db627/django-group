
# Tutorial on Migration, Models, Factory, seeding with fake data and testing the Data Base.
### Author: Elizabeth Oluwasanmi, Dennis Boguslavskiy, Bovan

### Introduction to Django
## To follow along use this repository: https://github.com/db627/django-tutorial
Django, a high-level Python web framework, is renowned for its "batteries-included" philosophy, providing developers with a robust set of tools for building web applications quickly and efficiently. In this article, we'll guide you through the process of creating a Django application from the ground up. We'll cover everything from setting up models to creating migrations, generating fake data with Factory Boy, and testing the database.

### Setting Up Django

Before diving into models and migrations, ensure that Django is installed in your Python environment. 
1. Clone The Repository
3. Setup a virtual enviornment
```
python3 -m venv .venv
source .venv/bin/activate
```
4. CD into the myapp folder
```
cd myapp
```
4. Install all necessary requirements
```
pip3 install -r requirements.txt
```

### Setting the Stage: The Model

In Django, a model represents the structure of a database table. Let's consider a simple example: a to-do application. In your models.py file, define a ToDo model:

Copy Code:
```
from django.db import models #import django models

class User(models.Model): #create a User model
    first_name = models.CharField(max_length=100) #Create a first Name field
    last_name = models.CharField(max_length=100) #Create a last name field
    email = models.EmailField(default='example@example.com', max_length=100) #Create an email field
    
    def __str__(self):
        return self.first_name
```
Migrations: Bringing Models to Life

Django uses migrations to manage database schema changes. After defining your model, run the following commands to create an initial migration and apply it to the database:
```
python manage.py makemigrations myapp
python manage.py migrate
```

This process ensures that your database is synchronized with your model.

Factory 
Factory boy is a fantastic library for generating test data. Let's create a factory for our ToDo model:
```
import factory
from faker import Faker
from myapp.models import User


fake = Faker()

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
    
    first_name = factory.LazyAttribute(lambda x: fake.first_name())
    last_name = factory.LazyAttribute(lambda x: fake.last_name())
    email = factory.LazyAttribute(lambda x: fake.email())


```
Note: This ToDo Factory generates instances of the ToDo model with fake text for the todo_item field.

Seeding the Database with Fake Data

Now, let's use our factory to seed the database with fake to-do items. In a Django management command or script, you can do the following:

# seed_data.py
```
from django.core.management.base import BaseCommand
from myapp.factories import UserFactory
class Command(BaseCommand):
    help = 'Seeds the database with User and Course data'

    def add_arguments(self, parser):
        parser.add_argument(
            '--users',
            type=int,
            help='Number of users to create'
        )


    def handle(self, *args, **kwargs):
        num_users = kwargs['users'] or 100  # Default to 100 if not specified
    
        self.stdout.write('Seeding {} users...'.format(num_users))
        UserFactory.create_batch(num_users)

        self.stdout.write(self.style.SUCCESS('Database seeding complete!'))
```
Testing the Database

Testing is a crucial aspect of development, and Django makes it easy to write tests for your database. Create a tests.py file in your app directory and add the following:

# tests.py
```
from django.test import TestCase
from myapp.models import ToDo

class ToDoModelTest(TestCase):
    def test_todo_creation(self):
        todo_item = 'Test ToDo Item'
        todo = ToDo.objects.create(todo_item=todo_item)
        self.assertEqual(todo.todo_item, todo_item)
```
Testing: 
1. Clone the repository .
2. Open terminal and run,
    ```
    cd myapp
    pip install -r requirements.txt
    ```
3. In the same terminal to migrate database run,
   ```
    Python manage.py make migrations myapp
    Python manage.py migrate
   ```
5. To seed database run
   ```
    Python manage.py seed
   ```
6. To test the database and CRUD operations  run, 
    ```
    pytest
    ```


Conclusion: 

In this journey through Django development, we've covered the creation of a model, the use of migrations to manage database changes, the integration of Factory Boy for generating test data, and the testing of our database functionality.
Django empowers developers to build robust web applications with ease, offering a seamless workflow from defining models to testing database functionality. Whether you're creating a to-do app or a more complex project, Django's comprehensive toolkit provides the foundation for efficient and reliable development.

 The article needs to explain the overall workflow of starting to program a backend with a database and how the concepts in the tutorial relate to each other.  
The tutorial is required to have a step-by-step guide for a user to implement the process.  
You should have a starting project with instructions to setup the install for the tutorial and a branch that has the completed tutorial to go with the article.


