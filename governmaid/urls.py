from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', 'governmaid.views.home', {'template':'landing.html'}),
    url(r'^hello/$', 'governmaid.views.hello', {'template':'hello.html'}),
    url(r'^login/$', 'governmaid.views.login', {'template':'login.html'}),
    url(r'^post/$', 'postapp.views.create_post', {'template':'create_post.html'}),
    url(r'^logout/$', 'governmaid.views.logout'),
    url(r'^create_post/$', 'postapp.views.create_post'),
    url(r'^process_create_post/$', 'postapp.views.process_create_post'),
    #url(r'^governmaid/', include('governmaid.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:

    url(r'^admin/', include(admin.site.urls)),

    url(r'^post/(?P<pk>)[0-9]+$', 'governmaid.views.home', {'template':'post_thread.html'}),

    url(r'^city/$', 'governmaid.views.city', {'template':'posts_for_town.html'}),

)
