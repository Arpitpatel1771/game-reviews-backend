from django.contrib import admin
from Todo.models import Task

class TaskAdmin(admin.ModelAdmin):
    fields = ["uuid", "title", "description", "status"]
    readonly_fields = ["uuid"]

admin.site.register(Task, TaskAdmin)