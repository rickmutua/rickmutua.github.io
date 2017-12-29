from django.urls import path
from . import views


urlpatterns = [

    path('', views.index, name='index'),

    path('projects/', views.project, name='projects'),

    path('tag/<str:tag_name>', views.tag, name='single-tag'),

    path('project/<str:project_name>', views.single_project, name='project'),

    path('contact/', views.contact, name='contact'),

]