# forms.py
from django import forms
from myapp.models import User, Course

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']

class UserDropdownForm(forms.Form):
    user = forms.ModelChoiceField(queryset=User.objects.all().order_by('first_name'))

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_name', 'course_section']
