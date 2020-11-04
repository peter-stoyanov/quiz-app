from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def quiz_page(request, uuid):
    return render(request, 'quiz.html')
