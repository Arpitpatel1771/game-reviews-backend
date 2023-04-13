from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from UserManagement.models import User, TestClass

# Register your models here.
admin.site.register(User, UserAdmin)

@admin.register(TestClass)
class TestClassAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]