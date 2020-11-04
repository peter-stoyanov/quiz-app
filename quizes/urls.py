from django.conf.urls import url

from quizes import views

urlpatterns = [
    url(r'(?P<uuid>[0-9a-zA-Z]{10,})', views.quiz_page)
]
