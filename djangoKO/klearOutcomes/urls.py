from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
	url(r'^bob$', views.bob, name='bob'),

	#url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
