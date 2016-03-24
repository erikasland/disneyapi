from django.conf.urls import url
from views import Index, SubmitValue
from apps.api.views import Api

urlpatterns = [
    url(r'^adddata/(?P<currdate>\d+)/(?P<prevdate>\d+)/(?P<val>\d+)$', Api.as_view()),
    url(r'^submitted/(?P<currdate>\d+)$', SubmitValue.as_view()),
    url(r'^$', Index.as_view())
]