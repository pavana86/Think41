from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Board, Column, Task
from .serializers import BoardSerializer

@api_view(['GET'])
def get_board_view(request, board_id):
    try:
        board = Board.objects.get(id=board_id)
        serializer = BoardSerializer(board)
        return Response(serializer.data)
    except Board.DoesNotExist:
        return Response({"error": "Board not found"}, status=404)

@api_view(['POST'])
def move_task(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
        new_column_id = request.data.get('column_id')
        new_order = request.data.get('order', 0)

        # Move to another column
        task.column_id = new_column_id
        task.order = new_order
        task.save()

        # Reorder tasks in that column
        tasks = Task.objects.filter(column_id=new_column_id).exclude(id=task_id).order_by('order')
        for index, t in enumerate(tasks, start=(1 if new_order == 0 else 0)):
            if index == new_order:
                index += 1
            t.order = index
            t.save()

        return Response({"message": "Task moved successfully"})
    except Task.DoesNotExist:
        return Response({"error": "Task not found"}, status=404)

@api_view(['POST'])
def reorder_tasks(request, column_id):
    task_order = request.data.get('task_order')  # List of task IDs in new order
    if not task_order:
        return Response({"error": "task_order list is required"}, status=400)

    for index, task_id in enumerate(task_order):
        Task.objects.filter(id=task_id, column_id=column_id).update(order=index)

    return Response({"message": "Tasks reordered successfully"})
class BoardView(api_view):
    def get(self, request, board_id):
        board = get_object_or_404(Board, pk=board_id)
        return Response({"id": board.id, "title": board.title})