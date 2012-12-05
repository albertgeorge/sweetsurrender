from django.conf.urls.defaults import patterns, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sweetsurrender.views.home', name='home'),
    url(r'^sweetsurrender/$', 'sweetsurrender.views.home', name='home_url'),
    url(r'^sweetsurrender/product/$', 'sweetsurrender.views.product', name='product_url'),
    url(r'^sweetsurrender/about/$', 'sweetsurrender.views.about',name='aboutus_url'),
    
    # url(r'^sweetsurrender/', include('sweetsurrender.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )
