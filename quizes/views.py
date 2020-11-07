from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from quizes.forms import QuizForm
from quizes.models import Quiz


def view_quiz(request, uuid):
    quiz = get_object_or_404(Quiz, uuid=uuid)
    return render(request, 'quiz.html', {'quiz': quiz})


def create_quiz(request):
    if request.method == "POST":
        form = QuizForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/quiz/all')
    else:
        form = QuizForm()
    return render(request, 'create_quiz.html', {'form': form})


def list_quizes(request):
    quizes = Quiz.objects.all()
    return render(request, 'list_quizes.html', {'quizes': quizes})
