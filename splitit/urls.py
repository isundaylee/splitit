from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'splitit.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^groups/(?P<group_id>\d+)$', 'groups.views.show', name='show_group'),
    url(r'^groups/(?P<group_id>\d+)/(?P<person_id>\d+)$', 'groups.views.show_person', name='show_person'),
    url(r'^groups/new$', 'groups.views.new', name='new_group'),
    url(r'^groups/$', 'groups.views.create', name='create_group'),
    url(r'^groups/(?P<group_id>\d+)/transactions/new$', 'transactions.views.new', name='new_transaction'),
    url(r'^groups/(?P<group_id>\d+)/transactions/$', 'transactions.views.create', name='create_transaction'),
    url(r'^$', 'groups.views.index', name='groups'),
)
