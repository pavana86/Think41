
# Create your models here.
from django.db import models

class Board(models.Model):
    title = models.CharField(max_length=255)

class Column(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='columns')
    title = models.CharField(max_length=255)
    order = models.IntegerField()

class Task(models.Model):
    column = models.ForeignKey(Column, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=255)
    order = models.IntegerField()