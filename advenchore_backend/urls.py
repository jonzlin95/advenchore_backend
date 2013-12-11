from django.conf.urls import patterns, include, url
from advenchore_backend import views


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'advenchore_backend.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^family/$', views.FamilyList.as_view()),
    url(r'^family/(?P<pk>[0-9]+)/$', views.FamilyDetail.as_view()),
)
