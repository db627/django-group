from django.conf import settings
from django.db import models

class ToDo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    todo_item = models.CharField(max_length=100)
    
    def __str__(self):
        return self.todo_item


    
class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_section = models.CharField(max_length=100)

    def __str__(self):
        return self.course_name


