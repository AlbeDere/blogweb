from django.urls import path
from . import views

urlpatterns = [
    path("", views.blog_index, name="blog_index"),
    path("post/<int:pk>/", views.blog_detail, name="blog_detail"),
    path("category/<category>/", views.blog_category, name="blog_category"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("register", views.register, name="register"),
    path("login_view", views.login_view, name="login_view"),
    path("logout_view", views.logout_view, name="logout_view"),
    path('delete/<int:post_id>/', views.delete_post, name='delete_post'),
    path("create_blogpost", views.create_blogpost, name="create_blogpost"),
    path('edit_blogpost/<int:post_id>/', views.edit_blogpost, name='edit_blogpost'),
]