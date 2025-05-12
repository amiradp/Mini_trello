# projects/admin.py

from django.contrib import admin
from .models import Project, Task

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'created')
    search_fields = ('title', 'description', 'owner')
    list_filter = ('created', 'owner')

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'status', 'created', 'deadline')
    search_fields = ('title', 'description', 'project', 'deadline')
    list_filter = ('status', 'created', 'deadline')
