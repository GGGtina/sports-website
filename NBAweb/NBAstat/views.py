from django.http import HttpResponse
from django.shortcuts import render

import datetime


def hello(request):
    return HttpResponse("Hello world!")


def hello_tmp(request):
    today = datetime.datetime.now().date()
    return render(request, "hello.html", {"today": today})
