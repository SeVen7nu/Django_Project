from . import views
from django.urls import path

app_name = 'devops'

urlpatterns = [
    path('login/', views.login),
    path('index/', views.index),
    path('register/', views.register),
    path('logout/', views.logout),
    path('add-host/', views.add_host),
    path('edit-host/', views.edit_host),
    path('delete-host/', views.delete_host),
]
