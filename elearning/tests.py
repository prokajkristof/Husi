from django.test import TestCase, Client
import datetime
from django.urls import reverse, resolve

from elearning.models import Course, Instructor, Student


class InstructorTest(TestCase):
    def test_fields(self):
        instructor = Instructor()
        instructor.first_name= "Test First"
        instructor.last_name = "Test Last"
        instructor.email = "Test Email"
        instructor.registration_date = datetime.datetime.now()
        instructor.num_of_published_courses = 1
        instructor.num_of_enrolled_students = 1
        instructor.average_review_rating = 3
        instructor.num_of_reviews = 1
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
        student.num_of_courses_enrolled = 1
        student.num_of_courses_completed = 1
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


