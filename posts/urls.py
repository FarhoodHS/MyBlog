from django.urls import path
from .views import (
    post_list,
    user_post_list,
    post_create,
    post_detail,
    post_update,
    post_delete,
)

app_name = 'posts'

urlpatterns = [
    path('', post_list, name='post_list'),
    path('create', post_create, name='post_create'),
    path('user/<slug:author>', user_post_list, name='user_post_list'),
    path('<slug:post_slug>', post_detail, name='post_detail'),
    path('<slug:post_slug>/edit', post_update, name='post_update'),
    path('<slug:post_slug>/delete', post_delete, name='post_delete'),
]
