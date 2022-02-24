from django.urls import path

from app.views import TodoListandCreate, TodoListUpdateandDelete

urlpatterns = [
    path('', TodoListandCreate.as_view()),
    path('<int:pk>/', TodoListUpdateandDelete.as_view())
]