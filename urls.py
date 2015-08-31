from django.conf.urls import url, patterns
from httpproxy.views import HttpProxy
import api, jabong

urlpatterns = patterns(
    '',
    url(r'^$', api.test, name='test'),

    url(r'^jabong/test_insert$', api.test_insert, name='test_insert'),
    url(r'^jabong/form$', jabong.get_form, name='jabong.form'),
    url(r'^jabong/post$', jabong.post_form, name='jabong.post')
)