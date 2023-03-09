from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path("", views.hello, name="index"),
    path("login/", views.login, name="login"),
    path("profile/", views.profile, name="profile"),
    path("contact/", views.contact, name="contact"),
    path("features/", views.features, name="features"),
    path("c_index/", views.c_index, name="c_index"),
    path("c_intro/", views.c_intro, name="c_intro"),
    path("c_compile/", views.c_compile, name="c_compile"),
    path("c_started/", views.c_started, name="c_started"),
    path("c_syntax/", views.c_syntax, name="c_syntax"),
    path("c_print/", views.c_print, name="c_print"),
    path("c_variable/", views.c_variable, name="c_variable"),
    path("c_datatype/", views.c_datatype, name="c_datatype"),
    path("c_keyword/", views.c_keyword, name="c_keyword"),
    path("python/", views.python, name="python"),
    path("insertdata/", views.insertdata, name="insert"),

]
