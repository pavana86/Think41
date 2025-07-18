from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Board, Column, Task

admin.site.register(Board)
admin.site.register(Column)
admin.site.register(Task)
