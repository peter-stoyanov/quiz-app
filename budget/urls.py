from django.conf.urls import url

from budget import views

urlpatterns = [
    url(r'^$', views.create_expense),
    url(r'/all', views.all_expenses),
    # url(r'/(?P<uuid>[0-9A-Fa-f]{8}[-]?(?:[0-9A-Fa-f]{4}[-]?){3}[0-9A-Fa-fs]{12})', views.view_quiz)
]

