from django.db import models
from django.urls import reverse

class Instructor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, unique=True)
    registration_date = models.DateField()


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=255, unique=True)
    registration_date = models.DateField()


class Course(models.Model):
    course_title = models.CharField(max_length=200)
    course_brief = models.CharField(max_length=4000)
    instructor_id = models.IntegerField()
    num_of_chapters = models.IntegerField()

    def get_absolute_url(self):
        return reverse('course-list')


class CourseChapter(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    chapter_title = models.CharField(max_length=100)


class Enrollment(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateField()


class ContentType(models.Model):
    content_type = models.CharField(max_length=20)


class CourseChapterContent(models.Model):
    course_chapter_id = models.ForeignKey(CourseChapter, on_delete=models.CASCADE)
    content_type_id = models.ForeignKey(ContentType, on_delete=models.CASCADE)


class LearningProgress(models.Model):
    enrollment_id = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    course_chapter_content_id = models.ForeignKey(CourseChapterContent, on_delete=models.CASCADE)
    status = models.CharField(max_length=1)


class Feedback(models.Model):
    enrollment_id = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    rating_score = models.IntegerField()
    feedback_text = models.CharField(max_length=4000)
    submission_date = models.DateField()

