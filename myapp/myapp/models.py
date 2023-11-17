from django.db import models

class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_section = models.CharField(max_length=100)

    def __str__(self):
        return self.course_name

class ToDo(models.Model):
    todo_item = models.CharField(max_length=100)
    
    def __str__(self):
        return self.todo_item
    
