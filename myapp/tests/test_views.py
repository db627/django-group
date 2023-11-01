import pytest
from django.urls import reverse
from myapp.models import User, Course
from myapp.factory import UserFactory, CourseFactory

@pytest.fixture
def user():
    return UserFactory()

@pytest.fixture
def course():
    return CourseFactory()

@pytest.mark.django_db
def test_user_list_view(client):
    response = client.get(reverse('user_list'))
    assert response.status_code == 200

@pytest.mark.django_db
def test_user_create_view(client):
    user_count = User.objects.count()
    response = client.post(reverse('user_create'), {
        'first_name': 'John',
        'last_name': 'Doe',
    })
    assert response.status_code == 302
    assert User.objects.count() == user_count + 1

@pytest.mark.django_db
def test_user_update_view(client, user):
    response = client.post(reverse('user_update', kwargs={'pk': user.pk}), {
        'first_name': 'Jane',
        'last_name': 'Doe',
    })
    assert response.status_code == 302
    user.refresh_from_db()
    assert user.first_name == 'Jane'

@pytest.mark.django_db
def test_user_delete_view(client, user):
    user_count = User.objects.count()
    response = client.post(reverse('user_delete', kwargs={'pk': user.pk}))
    assert response.status_code == 302
    assert User.objects.count() == user_count - 1

@pytest.mark.django_db
def test_course_list_view(client):
    response = client.get(reverse('course_list'))
    assert response.status_code == 200

@pytest.mark.django_db
def test_course_create_view(client):
    course_count = Course.objects.count()
    response = client.post(reverse('course_create'), {
        'course_name': 'Intro to Django',
        'course_section': 'Web Development Basics',
    })
    assert response.status_code == 302
    assert Course.objects.count() == course_count + 1

@pytest.mark.django_db
def test_course_update_view(client, course):
    response = client.post(reverse('course_update', kwargs={'pk': course.pk}), {
        'course_name': 'Advanced Django',
        'course_section': 'Web Development Pro',
    })
    assert response.status_code == 302
    course.refresh_from_db()
    assert course.course_name == 'Advanced Django'

@pytest.mark.django_db
def test_course_delete_view(client, course):
    course_count = Course.objects.count()
    response = client.post(reverse('course_delete', kwargs={'pk': course.pk}))
    assert response.status_code == 302
    assert Course.objects.count() == course_count - 1
