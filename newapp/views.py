from django.shortcuts import render
from django.http import HttpResponse
from .import views
from .models import *

# Create your views here.

# index.html view


def hello(request):
    return render(request, "index.html")


def login(request):
    return render(request, "login.html")


def profile(request):
    return render(request, "profile.html")


def contact(request):
    return render(request, "contact.html")


def features(request):
    return render(request, "features.html")


def c_index(request):
    return render(request, "c/c_index.html")


def c_intro(request):
    return render(request, "c/c_intro.html")


def c_compile(request):
    return render(request, "c/c_compile.html")


def c_started(request):
    return render(request, "c/c_started.html")


def c_syntax(request):
    return render(request, "c/c_syntax.html")


def c_print(request):
    return render(request, "c/c_print.html")


def c_variable(request):
    return render(request, "c/c_variable.html")


def c_datatype(request):
    return render(request, "c/c_datatype.html")


def c_keyword(request):
    return render(request, "c/c_keyword.html")


def cpp_index(request):
    return render(request, "c/c++_index.html")


def python(request):
    return render(request, "python.html")


def insertdata(request):
    # data come html to view
    Fname = request.POST['fname']
    Lname = request.POST['lname']
    Email = request.POST['email']
    contact = request.POST['contact']
    password = request.POST['password']


# creating object of model class
    newuser = users.objects.create(firstname=Fname, lastname=Lname,
                                   Email=Email, contact=contact,
                                   password=password)
# after insert show .html
    return render(request, "index.html")
