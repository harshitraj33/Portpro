from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin-panel/', include('accounts_app.urls', namespace='accounts')),
    path('', include('projects_app.urls', namespace='projects_app')),
    path('contact/', include('contact_app.urls', namespace='contact')),
    path('api/', include('api_app.urls', namespace='api')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
