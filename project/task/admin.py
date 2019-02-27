from django.contrib import admin
from task.models import Course,Student,Teacher;
# Register your models here.
admin.site.register([Student,Teacher,Course]);