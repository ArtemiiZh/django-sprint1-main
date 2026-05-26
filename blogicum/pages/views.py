from django.http import HttpResponse
from django.shortcuts import render


def about(request) -> HttpResponse:
    return render(request, 'pages/about.html')


def rules(request) -> HttpResponse:
    return render(request, 'pages/rules.html')
