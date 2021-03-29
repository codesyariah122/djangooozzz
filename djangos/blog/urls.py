from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^story/', views.story),
	url(r'^news/', views.news),
	url(r'^$', views.index)
]