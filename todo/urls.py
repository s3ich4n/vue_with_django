from django.urls import path

from . import views

app_name = 'todo'

urlpatterns = [
    # path('', views.TodoVue.as_view(), name='vue'),
    path('create/', views.TodoCreateV.as_view(), name='create'),
    path('list/', views.TodoListV.as_view(), name='list'),
    path('<int:pk>/delete/', views.TodoDeleteV.as_view(), name='delete')
]