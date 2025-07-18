from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Board, Task, Column
from .serializers import BoardSerializer

class BoardView(APIView):
    def get(self, request, board_id):
        board = get_object_or_404(Board, id=board_id)
        serializer = BoardSerializer(board)
        return Response(serializer.data)

class MoveTaskView(APIView):
    def post(self, request, task_id):
        task = get_object_or_404(Task, id=task_id)
        target_column_id = request.data.get('target_column_id')
        new_order = request.data.get('new_order', 0)

        target_column = get_object_or_404(Column, id=target_column_id)
        task.column = target_column
        task.order = new_order
        task.save()

        return Response({"message": "Task moved successfully"})

class ReorderTasksView(APIView):
    def post(self, request, column_id):
        tasks_order = request.data.get('task_ids')  # list of task IDs in new order
        for index, task_id in enumerate(tasks_order):
            task = get_object_or_404(Task, id=task_id)
            task.order = index
            task.save()
        return Response({"message": "Tasks reordered successfully"})