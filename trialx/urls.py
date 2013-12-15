from django.conf.urls import patterns, url
from trialx import views

urlpatterns = patterns('',
        url(r'^$', views.random_trial, name='random_trial'),
)