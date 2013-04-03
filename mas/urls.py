from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^save_sleep_journal$', 'rpm.views.save_sleep_journal', name='save_sleep_journal'),
    url(r'^save_blood_pressure$', 'rpm.views.save_blood_pressure', name='save_blood_pressure'),
    url(r'^fetch_bp_data/(?P<limit>\d*)$', 'rpm.views.fetch_bp_data', name='fetch_bp_data'),
    # url(r'^mas/', include('mas.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

#urlpatterns += staticfiles_urlpatterns()