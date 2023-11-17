import pytest
from django.urls import reverse
from myapp.models import Course
from myapp.factory import CourseFactory


@pytest.fixture
def course():
    return CourseFactory()

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
