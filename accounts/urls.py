from django.conf.urls import url

from accounts import views

urlpatterns = [
    url('register', views.register),
    url('login', views.login),
    url('logout', views.logout),
    url('add_to_session', views.add_to_session),
    url('session', views.session),
]

