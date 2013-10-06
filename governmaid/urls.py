from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
	url(r'^$', 'governmaid.views.home', {'template':'open.html'}),
	url(r'^landing$', 'governmaid.views.home', {'template':'landing.html'}),
	url(r'^hello/$', 'governmaid.views.hello', {'template':'hello.html'}),
	url(r'^login/$', 'governmaid.views.login', {'template':'login.html'}),
	url(r'^logout/$', 'governmaid.views.logout'),
	url(r'^process_create_post/$', 'postapp.views.process_create_post'),
    #url(r'^governmaid/', include('governmaid.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
	url(r'^city/$', 'governmaid.views.home', {'template':'postsForTown.html'}),
	url(r'^admin/', include(admin.site.urls)),
)
