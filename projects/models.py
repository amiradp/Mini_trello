from django.db import models
from django.conf import settings

class Project(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Task(models.Model):
    TASK_STATUS = [
        ('1', 'TODO'),
        ('2', 'IN_PROGRESS'),
        ('3', 'DONE')
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    status = models.CharField(max_length=10, choices=TASK_STATUS, blank=True, verbose_name='Whats is your status?', default='1')

    deadline = models.DateField(null=True, blank=True)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.status}"


