from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from .views import *
from django.conf import settings
from django.conf.urls.static import static
# app_name = "blog"
urlpatterns = [
    path('dashboard',home, name="home" ),
    path('',login, name="login" ),
    path('register',register, name="register" ),
    path('detail',detail, name="detail" ),
    path('add_blog',add_blog, name="add_blog" ),
    path('logout_view',logout_view, name="logout_view" ),
    path('blog_detail/<slug>',blog_detail,name="blog_detail"),
    path('see_blog',see_blog,name="see_blog"),
    path('delete_blog/<id>',delete_blog,name="delete_blog"),
    path('update_blog/<slug>',update_blog,name="update_blog"),



]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)