from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DeleteView

from todo.models import Todo

"""
RedirectView 를 제외한 모든 뷰가 template_name 이 있다.
CreateView 는:
Form, field, success 시의 값이 필요하다!

DeleteView 는:
success_url 로 reverse_lazy 하는 편이 더 좋다.
"""


class TodoVue(TemplateView):
    template_name = 'todo/vue_main.html'


class TodoCreateV(CreateView):
    model = Todo
    fields = '__all__'
    template_name = 'todo/todo_form.html'
    success_url = reverse_lazy('todo:list')


class TodoListV(ListView):
    model = Todo
    template_name = 'todo/todo_list.html'


class TodoDeleteV(DeleteView):
    model = Todo
    template_name = 'todo/todo_confirm_delete.html'
    success_url = reverse_lazy('todo:list')
