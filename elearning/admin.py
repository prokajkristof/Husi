from django.contrib import admin
from elearning.models import Instructor, Student, Course, CourseChapter, Enrollment, ContentType, CourseChapterContent, LearningProgress, Feedback


admin.site.register(Instructor)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(CourseChapter)
admin.site.register(Enrollment)
admin.site.register(ContentType)
admin.site.register(CourseChapterContent)
admin.site.register(LearningProgress)
admin.site.register(Feedback)
