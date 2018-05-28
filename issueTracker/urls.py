from django.conf.urls import url
from issueTracker.views import issueView,issueTracker
 
urlpatterns = [
    url(r'^$', issueView.as_view()),
    url(r'(?P<pk>[0-9]+)/$', issueView.as_view()),
    url(r'issue', issueView.as_view()),
    ]