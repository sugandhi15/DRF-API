from django.urls import path
from . import views
from .views import TodoView
from .views import TodoViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'todo-view-set',TodoViewSet, basename='todoviewset')

urlpatterns = [
    path('',views.homepage,name="homepage"),
    path("post_todo",views.post_todo,name="post_todo"),
    path("get_todo",views.get_todo,name="get_todo"),
    path("patch_todo",views.patch_todo,name="patch_todo"),

    path('todo/',TodoView.as_view()),
]

urlpatterns += router.urls

