from django.shortcuts import render, redirect, get_object_or_404
from myapp.models import User, Course, ToDo
from myapp.forms import UserForm, CourseForm, ToDoForm

def index(request):
    return render(request, 'index.html')

def pageone(request):
    return render(request, 'pageone.html')

def pagetwo(request):
    return render(request, 'pagetwo.html')

def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})

def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm()
    return render(request, 'user_form.html', {'form': form})

def user_update(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm(instance=user)
    return render(request, 'user_form.html', {'form': form})

def user_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')
    return render(request, 'user_confirm_delete.html', {'user': user})

# Course Views

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

def add_todo_view(request):
    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_todo')
    else:
        form = ToDoForm()
    return render(request, 'add_todo.html', {'form': form})

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
def delete_todo_view(request, todo_id):
    ToDo.objects.get(pk=todo_id).delete()
    return redirect('list_todo')
def list_todo_view(request):
    todos = ToDo.objects.all()
    return render(request, 'list_todo.html', {'todos': todos})

