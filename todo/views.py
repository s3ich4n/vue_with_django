from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DeleteView
from django.views.generic.list import MultipleObjectMixin

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


# ccbv.co.uk 의 상속객체 사진파일 참조
# 상속 순서도 중요하다!
# listview는 get만 구현되어있지만, createview는 get, post 등이 먼저 구현되어있다.
# 따라서 상속된 것이 더 많은 createview부터 써주는 것이 에러 가능성을 줄이는 방법이다.

# mixin, main 순으로 상속받는 것이 좋다.

# 대부분의 기능은 CreateView에서 처리하고,
# object_list를 템플릿에 넘겨주는 기능은 mixin이 수행한다.
# self.object_list를 해당 class-based views에 추가해둬야 사용가능하다.
class TodoMOMCV(MultipleObjectMixin, CreateView):
    model = Todo
    fields = '__all__' # 필드속성
    template_name = 'todo/todo_form_list.html'
    success_url = reverse_lazy('todo:mixin')

    # object.list 컨텍스트 변수를 사용하기 위해서는 다음과정을 수행한다.
    def get(self, request, *args, **kwargs):

        # 1. get_queryset을 object_list에 오버라이드한다.
        # DB에서 레코드를 가져오는 함수
        # MultipleObjectMixin, CreateView 순으로 get_queryset 을 찾아서 사용.
        self.object_list = self.get_queryset()

        # 기반 클래스의 메소드를 호출해서 중복을 줄인다.
        # 보통은 매개변수를 똑같이 입력한다.
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        return super().get(request, *args, **kwargs)
