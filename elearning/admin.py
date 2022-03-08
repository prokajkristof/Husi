from django.contrib import admin
from elearning.models import Instructor, Student, Course, CourseChapter, Enrollment


admin.site.register(Instructor)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(CourseChapter)
admin.site.register(Enrollment)

