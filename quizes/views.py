from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from quizes.models import Quiz


def view_quiz(request, uuid):
    quiz = get_object_or_404(Quiz, uuid=uuid)
    return render(request, 'quiz.html', {'quiz': quiz})


def create_quiz(request):
    return render(request, 'create_quiz.html')
