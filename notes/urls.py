from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create),
    path('update', views.update),
    path('delete', views.delete),
    path('tags', views.tags, name='tags'),
    path('inicio', views.index),
    path('get-tag', views.tag),
    path('delete-tag', views.delete_tag),
    path('update-tag', views.update_tag)
]