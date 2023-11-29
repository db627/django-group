
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('pageone/', views.pageone, name="pageone"),
    path('pagetwo/', views.pagetwo, name="pagetwo"),
    path('courses/', views.course_list, name='course_list'),
    path('course/create/', views.course_create, name='course_create'),
    path('course/update/<int:pk>/', views.course_update, name='course_update'),
    path('course/delete/<int:pk>/', views.course_delete, name='course_delete'),
    path('todo/', views.list_todo_view, name='list_todo'),
    path('add/', views.add_todo_view, name='add_todo'),
    path('update/<int:todo_id>/', views.update_todo_view, name='update_todo'),
    path('delete/<int:todo_id>/', views.delete_todo_view, name='delete_todo'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
