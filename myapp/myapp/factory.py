import factory
from faker import Faker
from myapp.models import Course, ToDo


fake = Faker()

class CourseFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Course
    
    course_name = factory.LazyAttribute(lambda x: fake.bs())  
    course_section = factory.LazyAttribute(lambda x: fake.bothify(text="Section ##"))  

class ToDoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ToDo
    
    todo_item = factory.LazyAttribute(lambda x: fake.bs())