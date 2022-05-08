from django.urls import re_path
from tutorials import views

urlpatterns = [
    re_path(r'^api/tutorials$', views.tutorial_list),
    re_path(r'^api/tutorials/(?P<pk>[0-9]+)$', views.tutorial_details),
    re_path(r'^api/tutorials/published$', views.tutorial_list_published),
]