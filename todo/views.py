from django.views.generic import TemplateView


class TodoVue(TemplateView):
    template_name = 'vue.html'
