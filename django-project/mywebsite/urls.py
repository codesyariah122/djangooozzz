from django.conf.urls import url
from django.contrib import admin
from . import views
from blog import views as blogViews

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^blog/$', blogViews.index),

    url(r'^$', views.index)
]
