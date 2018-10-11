from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from snippets.views import snippet_list, snippet_detail, SnippetList, SnippetDetail, UserList, UserDetail, api_root, \
    SnippetHighlight

urlpatterns = [
    url(r'^snippets/$', snippet_list),
    url(r'^snippets/(?P<pk>[0-9]+)/$', snippet_detail),
]

urlpatterns = [
    url(r'^snippets/$', SnippetList.as_view(), name='snippet-list'),
    url(r'^snippets/(?P<pk>[0-9]+)/$', SnippetDetail.as_view(), name='snippet-detail'),
    url(r'^users/$', UserList.as_view(), name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', UserDetail.as_view(), name='user-detail'),
]

# urlpatterns = urlpatterns + [
#     # url(r'^$', api_root),
#     url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', SnippetHighlight.as_view(), name='snippet-highlight'),
# ]

urlpatterns = format_suffix_patterns(urlpatterns)
