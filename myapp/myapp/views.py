from django.shortcuts import render, redirect, get_object_or_404
from myapp.models import Course, ToDo
from myapp.forms import CourseForm, ToDoForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html')

def pageone(request):
    return render(request, 'pageone.html')

def pagetwo(request):
    return render(request, 'pagetwo.html')

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})

def course_create(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'course_form.html', {'form': form})

def course_update(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm(instance=course)
    return render(request, 'course_form.html', {'form': form})

def course_delete(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        course.delete()
        return redirect('course_list')
    return render(request, 'course_confirm_delete.html', {'course': course})

@login_required
def todo_view(request):
    if request.method == 'POST':
        if 'add' in request.POST:
            form = ToDoForm(request.POST)
            if form.is_valid():
                form.save()
        elif 'update' in request.POST:
            updated_item = ToDo.objects.get(pk=request.POST.get('todo_id'))
            form = ToDoForm(request.POST, instance=updated_item)
            if form.is_valid():
                form.save()
        elif 'delete' in request.POST:
            todo_id = request.POST.get('todo_id')
            ToDo.objects.get(pk=todo_id).delete()
        return redirect('todo_view')
    
    else:
        todos = ToDo.objects.all()
        form = ToDoForm()
    
    return render(request, 'todo.html', {'form': form, 'todos': todos})

@login_required
def add_todo_view(request):
    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_todo')
    else:
        form = ToDoForm()
    return render(request, 'add_todo.html', {'form': form})

@login_required
def update_todo_view(request, todo_id):
    todo_item = ToDo.objects.get(pk=todo_id)
    if request.method == 'POST':
        form = ToDoForm(request.POST, instance=todo_item)
        if form.is_valid():
            form.save()
            return redirect('list_todo')
    else:
        form = ToDoForm(instance=todo_item)
    return render(request, 'update_todo.html', {'form': form, 'todo_item': todo_item})

@login_required
def delete_todo_view(request, todo_id):
    ToDo.objects.get(pk=todo_id).delete()
    return redirect('list_todo')

@login_required
def list_todo_view(request):
    todos = ToDo.objects.all()
    return render(request, 'list_todo.html', {'todos': todos})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # Log the user in
            return redirect('list_todo')  # Redirect to a home page
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('list_todo')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')  