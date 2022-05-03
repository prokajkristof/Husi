from django.test import TestCase, Client
import datetime
from django.urls import reverse, resolve
from elearning.views import CourseListView
from elearning.models import Course, Instructor, Student


class InstructorTest(TestCase):
    def test_fields(self):
        instructor = Instructor()
        instructor.first_name= "Test First"
        instructor.last_name = "Test Last"
        instructor.email = "Test Email"
        instructor.registration_date = datetime.datetime.now()
        instructor.save()

        record = Instructor.objects.get(id=1)
        self.assertEqual(record, instructor)


class StudentTest(TestCase):
    def test_fields(self):
        student = Student()
        student.first_name = "Test First"
        student.last_name = "Test Last"
        student.email = "Test Email"
        student.registration_date = datetime.datetime.now()
        student.save()

        record = Student.objects.get(id=1)
        self.assertEqual(record, student)


class CourseTest(TestCase):
    def test_fields(self):
        course = Course()
        course.course_title = "Test Title"
        course.course_brief = "Test Brief"
        course.instructor_id = 1
        course.num_of_chapters = 1
        course.save()

        record = Course.objects.get(id=1)
        self.assertEqual(record, course)

    def test_get_absolute_url(self):
        course = Course()
        course.course_title = "Test Title"
        course.course_brief = "Test Brief"
        course.instructor_id = 1
        course.num_of_chapters = 1
        course.save()
        course = Course.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEqual(course.get_absolute_url(), '/course_list/')


class CourseListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 13 authors for pagination tests
        number_of_courses = 13

        for course_id in range(number_of_courses):
            Course.objects.create(
                course_title=f'Test {course_id}',
                course_brief=f'Test {course_id}',
                instructor_id=1,
                num_of_chapters=1
            )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/course_list/')
        self.assertEqual(response.status_code, 200)


    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('course-list'))
        self.assertEqual(response.status_code, 200)


    def test_pagination_is_ten(self):
        response = self.client.get(reverse('course-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] != True)
