from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from domains import views


# API endpoints
urlpatterns = format_suffix_patterns([

    url(r'^domains/$',
        views.DomainList.as_view(),
        name='domain-list'),
    url(r'^domains/(?P<pk>[0-9]+)/$',
        views.DomainDetail.as_view(),
        name='domain-detail'),
])

# Login and logout views for the browsable API
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]