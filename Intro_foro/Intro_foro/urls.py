from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('autenticacion.urls')),
    path('', include('apps.network.urls', namespace ='network'))
#    path('', include('apps.network.urls', namespace='network'))  #no la estoy usando
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)