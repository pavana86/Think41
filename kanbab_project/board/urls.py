from django.urls import path
from .views import BoardView, MoveTaskView, ReorderTasksView

urlpatterns = [
    path('board/<int:board_id>/view/', BoardView.as_view()),
    path('task/<int:task_id>/move/', MoveTaskView.as_view()),
    path('column/<int:column_id>/reorder/', ReorderTasksView.as_view()),]
