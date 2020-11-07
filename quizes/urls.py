from django.conf.urls import url

from quizes import views

urlpatterns = [
    url(r'^$', views.create_quiz),
    url(r'/(?P<uuid>[0-9A-Fa-f]{8}[-]?(?:[0-9A-Fa-f]{4}[-]?){3}[0-9A-Fa-fs]{12})', views.view_quiz)
]

