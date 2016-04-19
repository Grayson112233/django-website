# Import basic django url class
from django.conf.urls import url
# Import views form the poll app (this directory)
from . import views

urlpatterns = [
	# This object constuctor is taking a regex, the index
	# view function, and the name 'index' 
	url(r'^$', views.index, name="index"),
        url(r'^(?P<question_id>[0-9]+)/$', views.detail, name="detail"),
        url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name="results"),
        url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name="vote"),
]

