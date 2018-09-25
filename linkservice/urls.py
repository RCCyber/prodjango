from django.conf.urls import url
from django.views.generic import ListView, DetailView
from linkservice.models import LinkBase
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
#    url(r'^request/$', views.in_request, name='in_request'),
    url(r'^in_request/$', ListView.as_view(queryset=LinkBase.objects.all(), template_name="linkservice/out.html")),
    url(r'^(?P<pk>\d+)$', DetailView.as_view(model= LinkBase, template_name="in_request/out.html"))
]
