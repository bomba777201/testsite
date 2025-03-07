from django.shortcuts import render
from django.urls import path

def main_page(request):
    return render(request, 'main.html')

