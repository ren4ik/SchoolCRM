from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from handbook.views import DirectionList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('api.urls')),
    path('handbook/', include('handbook.urls')),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
