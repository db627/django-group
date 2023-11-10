from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(default='example@example.com', max_length=100)

    def __str__(self):
        return self.first_name

    
class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_section = models.CharField(max_length=100)

    def __str__(self):
        return self.course_name

class ToDo(models.Model):
    todo_item = models.CharField(max_length=100)
    
    def __str__(self):
        return self.todo_item
    
