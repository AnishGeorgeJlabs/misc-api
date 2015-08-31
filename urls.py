from django.conf.urls import url, patterns
from httpproxy.views import HttpProxy
import api

urlpatterns = patterns(
    '',
    url(r'^$', api.test, name='test'),
    url(r'^test_insert$', api.test_insert, name='test_insert')
)