from django.contrib import admin

from .models import Project, Task


@admin.register(Project)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner']

    inlines = [
        OrderItemInLine
    ]


@admin.register(Task)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'project', 'status', 'owner', ]
