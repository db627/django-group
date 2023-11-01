
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('pageone/', views.pageone, name="pageone"),
    path('pagetwo/', views.pagetwo, name="pagetwo"),
    path('users/', views.user_list, name='user_list'),
    path('user/create/', views.user_create, name='user_create'),
    path('user/update/<int:pk>/', views.user_update, name='user_update'),
    path('user/delete/<int:pk>/', views.user_delete, name='user_delete'),
    path('courses/', views.course_list, name='course_list'),
    path('course/create/', views.course_create, name='course_create'),
    path('course/update/<int:pk>/', views.course_update, name='course_update'),
    path('course/delete/<int:pk>/', views.course_delete, name='course_delete'),
]
