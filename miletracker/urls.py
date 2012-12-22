from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.defaults import patterns, url, include

from django.views.generic.simple import direct_to_template

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
   # (r'', include('miletracker.apps.')),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),

    url(r'^$',
        direct_to_template, {
            'template': 'landing.html',
            'extra_context': {},
        }, name='landing'),

    url(r'^add/$',
        'main.views.edit',
         name='add'),

    url(r'^edit/(?P<trip_id>[-\w]+)/$',
        'main.views.edit',
         name='edit'),

    url(r'^log/$',
        'main.views.log',
        name='log'),
)

if settings.DEBUG and settings.STATIC_ROOT:
    urlpatterns += static(settings.STATIC_URL,
        document_root=settings.STATIC_ROOT)

"""
urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^rewards/', include('rewards.urls')),
    (r'', include('social_auth.urls')),
    # sample reports
    url(r'^sample/credit-report/$',
        direct_to_template, {
            'template': 'aplicaciones/reports/report.html',
            'extra_context': {
                'sample': True, 'subtab':'tour', 'printable': True,
                'content_template': 'aplicaciones/reports/credit/credit_report_content.html',
                'report': parse_reports.parse_credit(get_all_sample.credit),
            }
        }, name='sample_credit_report'),

    url(r'^sample/criminal-report/$',
        direct_to_template, {
            'template': 'aplicaciones/reports/report.html',
            'extra_context': {
                'sample': True, 'subtab':'tour', 'printable': True,
                'content_template': 'aplicaciones/reports/criminal/criminal_report_content.html',
                'report': parse_reports.parse_criminal(get_all_sample.criminal),
            }
        }, name='sample_criminal_report'),

    url(r'^sample/eviction-report/$',
        direct_to_template, {
            'template': 'aplicaciones/reports/report.html',
            'extra_context': {
                'sample': True, 'subtab':'tour', 'printable': True,
                'content_template': 'aplicaciones/reports/eviction/eviction_report_content.html',
                'report': parse_reports.parse_eviction(get_all_sample.eviction),
            }
        }, name='sample_eviction_report'),

    # static pages
    url(r'^$', 'apps.views.home', name='home'),
    url(r'^refer/$', 'apps.views.refer', name='refer'),
    url(r'^linkedin/$', direct_to_template, {
            "template": "staticpages/linkedin.html",
            "extra_context": {'bypass': True,},
        }, name="linkedin"),
    url(r'^reddit/$', direct_to_template, {
            "template": "staticpages/reddit.html",
            "extra_context": {'bypass': True,},
        }, name="reddit"),
    url(r'^applicants/$', direct_to_template, {
            "template": "staticpages/for_applicants.html",
            "extra_context": {'bypass': True,},
        }, name="for_applicants"),
    url(r'^property-managers/$', direct_to_template, {
            "template": "staticpages/for_property_managers.html",
            "extra_context": {'bypass': True,},
        }, name="for_property_managers"),
    url(r'^agencies/$', direct_to_template, {
            "template": "staticpages/for_agencies.html",
            "extra_context": {},
        }, name="for_agencies"),
    url(r'^free-online-rental-applications-tour/$',
        direct_to_template, {
            'template': 'staticpages/tour.html',
            'extra_context': {
                'subtab': 'tour',
                'bypass': True,
            },
        }, name='tour'),
    url(r'^credit-criminal-eviction-checks-and-tenant-sreening/$',
        direct_to_template, {
            'template': 'staticpages/screening.html',
            'extra_context': {
                'subtab': 'screening',
                'bypass': True,
            }
        }, name='screening'),
    url(r'^the-benefits-of-online-apartment-applications/$',
        direct_to_template, {
            'template': 'staticpages/benefits.html',
            'extra_context': {
                'subtab': 'benefits',
                'bypass': True,
            }
        }, name='benefits'),
    url(r'^faq/$',
        direct_to_template, {
            'template': 'staticpages/faq.html',
            'extra_context': {
                'subtab': 'faq',
                'bypass': True,
            }
        }, name='faq'),
    url(r'^contact-us/$', 'apps.views.contact', name="contact_form"),
    # includes
    url(r'^app/', include('aplicaciones.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^dashboard/', include('dashboard.urls')),
    url(r'^rental/', include('rentals.urls')),
    url(r'^perms/', include('perms.urls')),
    url(r'^invites/', include('invites.urls')),
    url(r'^list/', include('mailchimp.urls')),
    url(r'^reports/', include('screening_reports.urls')),
    url(r'^forms/', include('freeforms.urls')),
    url(r'^fees/', include('appdoc_fees.urls')),
    url(r'^messages/', include('actions_store.urls')),

    # zip code api
    url(r'^findzip/$', 'apps.views.zipcode_to_citystate', name="findzip"),

    # object views
    url(r'^broker/view/(?P<slug>[-\w]+)/$',
        'accounts.profiles.view_broker', name='view_broker'),
    url(r'^agency/view/(?P<slug>[-\w]+)/$',
        'accounts.profiles.view_agency', name='view_agency'),
    url(r'^agency/view/(?P<slug>[-\w]+)/agents/$',
        'accounts.profiles.view_agency_brokers', name='view_agency_brokers'),
    url(r'^agency/view/(?P<slug>[-\w]+)/listings/$',
        'accounts.profiles.view_agency_rentals', name='view_agency_rentals'),
    url(r'^landlord/view/(?P<slug>[-\w]+)/$',
        'accounts.profiles.view_landlord', name='view_landlord'),
)

# temporary pages
urlpatterns += patterns('',
    url(r'^customizable-application-forms/$',
        direct_to_template, {
            'template': 'staticpages/customizable.html',
            'extra_context': {
                'subtab': 'customizable',
                'bypass': True,
            }
        }, name='customizable'),
)

# lazysignup
urlpatterns += patterns('accounts.views',
    url(r'^convert/$', 'convert', {
        # 'form_class': SimpleUserCreationForm,
        }, name='lazysignup_convert'),
)

# sitemaps
urlpatterns += patterns('',
    (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps.sitemaps}),
)
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        (r'^' + settings.FILE_UPLOAD_URL.strip("/") + '/(?P<path>.*)$',
         'django.views.static.serve',
         {'document_root': settings.FILE_UPLOAD_DIR, 'show_indexes': True}),
        (r'^raw_template/(?P<template>.*)',
         'django.views.generic.simple.direct_to_template'),
    )


urlpatterns += patterns('',
    # alias for non-rental appdoc for a seller
    url(r'^(?P<slug>\S+)/$', 'apps.aplicaciones.views.application_for_seller_no_rental',
        name="application_for_seller_no_rental"),
)
"""
