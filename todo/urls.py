from django.urls import path

from . import views

app_data = 'todo'
urlpatterns = [
    path('', views.TodoVue.as_view(), name='vue'),
]