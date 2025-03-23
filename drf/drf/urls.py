
from django.contrib import admin
from django.urls import path, include

#for image to start showing 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),  # Include user API endpoints
    path("", include("webapp.urls")),  # Webapp URLs
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
