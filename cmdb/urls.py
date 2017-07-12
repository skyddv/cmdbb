from django.conf.urls import url
from cmdb.views import index, detail, rr, vote

app_name = 'cmdb'

urlpatterns = [
    url(r'^$', index),
    url(r'^(?P<name>.+)/detail$', detail, name='skyddv'),
    url(r'^(?P<name>.+)/vote', vote, name='vote'),
    url(r'^rr$', rr, name='whaha'),

]