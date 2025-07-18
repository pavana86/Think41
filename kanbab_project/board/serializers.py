from rest_framework import serializers
from .models import Board, Column, Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'order']

class ColumnSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True)

    class Meta:
        model = Column
        fields = ['id', 'title', 'order', 'tasks']

class BoardSerializer(serializers.ModelSerializer):
    columns = ColumnSerializer(many=True)

    class Meta:
        model = Board
        fields = ['id', 'title', 'columns']