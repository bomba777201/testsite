from django.shortcuts import render
from django.urls import path
from 123.py import login, password
def main_page(request):
    return render(request, 'main.html', context={'login': login, 'password': password})


