from django.urls import path

from .views import NewList

urlpatterns = [
    path('', NewList.as_view(), name='new'),
]