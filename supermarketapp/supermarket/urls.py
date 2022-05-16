from django.contrib import admin
from django.urls import path, include
from .views import delete_view, list_view, create_view, detail_view, update_view, delete_view

urlpatterns = [
    path('', list_view, name='list'),
    path('create', create_view, name='create'),
    path('<uuid:id>/detail/', detail_view, name='detail'),
    path('<uuid:id>/update/', update_view, name='update'),
    path('<uuid:id>/delete/', delete_view, name='delete'),
]