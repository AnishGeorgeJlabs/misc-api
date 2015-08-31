from django.conf.urls import url, patterns
from httpproxy.views import HttpProxy

urlpatterns = patterns(
    '',
    url(r'^$', api.test, name='test'),
)