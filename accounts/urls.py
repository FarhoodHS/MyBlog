from django.urls import path
from . import views


app_name = 'accounts'

urlpatterns = [
    # path('dashboard', post_list, name='post_list'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
]
