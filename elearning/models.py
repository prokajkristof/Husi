from django.db import models


class Instructor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, unique=True)
    registration_date = models.DateField()
    num_of_published_courses = models.IntegerField()
    num_of_enrolled_students = models.IntegerField()
    average_review_rating = models.FloatField()
    num_of_reviews = models.IntegerField()


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=255, unique=True)
    registration_date = models.DateField()
    num_of_courses_enrolled = models.IntegerField()
    num_of_courses_completed = models.IntegerField()


class Course(models.Model):
    course_title = models.CharField(max_length=200)
    course_brief = models.CharField(max_length=4000)
    instructor_id = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    num_of_chapters = models.IntegerField()


class CourseChapter(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    chapter_title = models.CharField(max_length=100)


class Enrollment(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateField()


