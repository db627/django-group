# forms.py
from django import forms
from myapp.models import User, Course, ToDo

class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ['todo_item']
        
class UserForm(forms.ModelForm):
    first_name = forms.CharField(max_length=128, help_text="Please enter the user's first name.")
    last_name = forms.CharField(max_length=128, help_text="Please enter the user's last name.")
    email = forms.EmailField(max_length=128, help_text="Please enter the user's email.")
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class UserDropdownForm(forms.Form):
    user = forms.ModelChoiceField(queryset=User.objects.all().order_by('first_name'))

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_name', 'course_section']
