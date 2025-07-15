from django.contrib import admin # type: ignore
from .models import Task

# Register your models here.
admin.site.register(Task)

