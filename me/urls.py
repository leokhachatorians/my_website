from django.conf.urls import url
from me import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about$', views.about, name='about'),
    url(r'^resume$', views.resume, name='resume'),
    url(r'^projects$', views.projects, name='projects'),
    url(r'^login$', views.login, name='login'),
    url(r'^logout$', views.logout, name='logout'),
]
