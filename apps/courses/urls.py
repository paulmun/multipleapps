from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^create$', views.create, name = 'createcourse'),
    url(r'^courses/destroy/(?P<id>\d+)$', views.destroy, name = 'destroycourse'),
    url(r'^register$', views.register, name = 'registration'),
    url(r'^enroll$', views.enrollments, name = 'enrollments'),
]