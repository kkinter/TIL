from unicodedata import name
from django.urls import path
from . import views

# url namespaces
# url을 이름으로 분류하는 기능

app_name = "todos"

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("delete/<int:todo_pk>", views.delete, name="delete"),
    path("update/<int:todo_pk>", views.update, name="update"),
]
