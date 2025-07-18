from django.db import models

# Create your models here.
class Board(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.title

class Column(models.Model):
    board = models.ForeignKey(Board, related_name="columns", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    position = models.IntegerField()

class Task(models.Model):
    column = models.ForeignKey(Column, related_name="tasks", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    position = models.IntegerField()
 