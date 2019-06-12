from django.contrib import admin
from .models import Todo


# 등록하려면 데코레이터 쪽이 더 편하다!
@admin.register(Todo)
class TodoConfig(admin.ModelAdmin):
    list_display = ('id', 'name', 'todo')
