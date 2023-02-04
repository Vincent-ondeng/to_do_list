from django.urls import path
from .views import TasklList

urlpatterns = [
    path('', TasklList.as_view(), name='tasks')
]
