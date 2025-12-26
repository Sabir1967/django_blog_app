# blog/urls.py
from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView # new


urlpatterns = [ 

path("",                      BlogListView.as_view(),   name="home_url"),
path("post/<int:pk>/",        BlogDetailView.as_view(), name="post_detail"),
path("post/new/",             BlogCreateView.as_view(), name="post_new_url"), 
path("post/<int:pk>/edit/",   BlogUpdateView.as_view(), name="post_edit_url"), # new
path("post/<int:pk>/delete/", BlogDeleteView.as_view(), name="post_delete_url"), # new

]