import factory
from faker import Faker
from myapp.models import User, Course, ToDo


fake = Faker()

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
    
    first_name = factory.LazyAttribute(lambda x: fake.first_name())
    last_name = factory.LazyAttribute(lambda x: fake.last_name())
    email = factory.LazyAttribute(lambda x: fake.email())

class CourseFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Course
    
    course_name = factory.LazyAttribute(lambda x: fake.bs())  
    course_section = factory.LazyAttribute(lambda x: fake.bothify(text="Section ##"))  

class ToDoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ToDo
    
    todo_item = factory.LazyAttribute(lambda x: fake.bs())