from django.conf.urls import patterns, include, url
from advenchore_backend import views


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'advenchore_backend.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^get/family/$', views.FamilyList.as_view()),
    url(r'^get/family/(?P<pk>[0-9]+)/$', views.FamilyDetail.as_view()),
    url(r'^get/task/$', views.TaskList.as_view()),
    url(r'^get/task/(?P<pk>[0-9]+)/$', views.TaskDetail.as_view()),
    url(r'^get/child/$', views.ChildList.as_view()),
    url(r'^get/child/(?P<pk>[0-9]+)/$', views.ChildDetail.as_view()),
    url(r'^get/reward/$', views.RewardList.as_view()),
    url(r'^get/reward/(?P<pk>[0-9]+)/$', views.RewardDetail.as_view()),    

    #POST
    url(r'^post/family/$', views.FamilyListPOST.as_view()),
    url(r'^post/family/(?P<pk>[0-9]+)/$', views.FamilyDetailPOST.as_view()),
    url(r'^post/task/$', views.TaskListPOST.as_view()),
    url(r'^post/task/(?P<pk>[0-9]+)/$', views.TaskDetailPOST.as_view()),
    url(r'^post/child/$', views.ChildListPOST.as_view()),
    url(r'^post/child/(?P<pk>[0-9]+)/$', views.ChildDetailPOST.as_view()),
    url(r'^post/reward/$', views.RewardListPOST.as_view()),
    url(r'^post/reward/(?P<pk>[0-9]+)/$', views.RewardDetailPOST.as_view()),    
 
    #OtherThings
    url(r'^get/task/child/(?P<pk>[0-9]+)/$', views.TasksOfChild.as_view()),    
    url(r'^get/task/parent/(?P<pk>[0-9]+)/$', views.TasksOfChild.as_view()),    
    url(r'^get/reward/child/(?P<pk>[0-9]+)/$', views.RewardsOfChild.as_view()),    
    url(r'^get/reward/parent/(?P<pk>[0-9]+)/$', views.RewardsOfParent.as_view()),    
)


