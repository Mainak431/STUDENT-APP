from django.contrib import admin
from .models import Post
from .models import Course
from .models import marks
from .models import Subwise_marks,faculty,department

admin.site.register(Post)
admin.site.register(Course)
admin.site.register(marks)
admin.site.register(Subwise_marks)
admin.site.register(department)
admin.site.register(faculty)
