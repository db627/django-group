# forms.py
from django import forms
from myapp.models import Course, ToDo

class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ['todo_item']
        
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_name', 'course_section']
