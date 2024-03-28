from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('like/<int:primary_key>', views.like, name='like')
]