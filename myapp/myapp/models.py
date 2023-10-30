from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name

    @classmethod
    def create(cls, first_name, last_name):
        user = cls(first_name=first_name, last_name=last_name)
        user.save()
        return user

    def update(self, first_name=None, last_name=None):
        if first_name:
            self.first_name = first_name
        if last_name:
            self.last_name = last_name
        self.save()

    def delete_user(self):
        self.delete()

    @classmethod
    def retrieve_by_id(cls, id):
        try:
            return cls.objects.get(id=id)
        except cls.DoesNotExist:
            return None
    
class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_section = models.CharField(max_length=100)

    def __str__(self):
        return self.course_name

    @classmethod
    def create(cls, course_name, course_section):
        course = cls(course_name=course_name, course_section=course_section)
        course.save()
        return course

    def update(self, course_name=None, course_section=None):
        if course_name:
            self.course_name = course_name
        if course_section:
            self.course_section = course_section
        self.save()

    def delete_course(self):
        self.delete()

    @classmethod
    def retrieve_by_id(cls, id):
        try:
            return cls.objects.get(id=id)
        except cls.DoesNotExist:
            return None
