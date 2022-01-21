from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from core.views import home

urlpatterns = [
    path('', home, name="api-routes"),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/core/', include('core.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name="obtain-token"),
    path('api/token/refresh/', TokenRefreshView.as_view(), name="refresh-token")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
