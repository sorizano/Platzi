from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'miniplataforma.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'clases.views.home', name='home'),
    url(r'^cargar-contenido-clase/(?P<id>\d+)$', 'clases.views.cargar_clase', name='cargar_clase'),
    url(r'^guardar-pregunta/$', 'discusion.views.guardar_pregunta'),
    url(r'^cargar-respuestas/(?P<id>\d+)$', 'discusion.views.cargar_respuestas'),
    url(r'^guardar-respuesta/$','discusion.views.guardar_respuesta'),
)
