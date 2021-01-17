from django.conf.urls import url

from formsets import views

urlpatterns = [
    url(r'^$', views.forms_home),
    url(r'/article', views.article_form),
]
