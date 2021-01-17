from django.shortcuts import render, redirect

# Create your views here.
from formsets.forms import ArticleForm


def forms_home(request):
    return render(request, 'home.html')


def article_form(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return redirect('/forms')
    else:
        form = ArticleForm()
    return render(request, 'article.html', {'form': form})
