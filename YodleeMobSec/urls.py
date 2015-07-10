from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^$', 'YodleeMobSec.views.index', name='index'),
    url(r'^Upload/$', 'YodleeMobSec.views.Upload', name='Upload'),
    url(r'^about/$', 'YodleeMobSec.views.about', name='about'),
    url(r'^error/$', 'YodleeMobSec.views.error', name='error'),
    url(r'^features/$', 'YodleeMobSec.views.features', name='features'),
    url(r'^ZIP_FORMAT/$', 'YodleeMobSec.views.ZIP_FORMAT', name='ZIP_FORMAT'),
    url(r'^MAC_ONLY/$', 'YodleeMobSec.views.MAC_ONLY', name='MAC_ONLY'),
    url(r'^StaticAnalyzer/$', 'StaticAnalyzer.views.StaticAnalyzer', name='StaticAnalyzer'),
    url(r'^StaticAnalyzer_iOS/$', 'StaticAnalyzer.views.StaticAnalyzer_iOS', name='StaticAnalyzer_iOS'),
    url(r'^ViewSource/$', 'StaticAnalyzer.views.ViewSource', name='ViewSource'),
    url(r'^ViewFile/$', 'StaticAnalyzer.views.ViewFile', name='ViewFile'),
    url(r'^Smali/$', 'StaticAnalyzer.views.Smali', name='Smali'),
    url(r'^Java/$', 'StaticAnalyzer.views.Java', name='Java'),
    url(r'^Search/$', 'StaticAnalyzer.views.Search', name='Search'),
    url(r'^ManifestView/$', 'StaticAnalyzer.views.ManifestView', name='ManifestView'),
    url(r'^DynamicAnalyzer/$', 'DynamicAnalyzer.views.DynamicAnalyzer', name='DynamicAnalyzer'),
    url(r'^InternalUpload/$', 'DynamicAnalyzer.views.InternalUpload', name='InternalUpload'),
    url(r'^View/$', 'DynamicAnalyzer.views.View', name='View'),
    url(r'^admin/', include(admin.site.urls)),
]



