from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.schemas import get_schema_view
from drf_yasg.views import get_schema_view as drf_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

schema_view = drf_schema_view(
    openapi.Info(
        title="Fast Food API",
        description="APi Descripshin",
        default_version="v1",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="hello@example.com")
    ),
    public=True,
    permission_classes=(AllowAny,)
)

urlpatterns = [
    path('api/v1/', include('api.urls')),
    path('admin/', admin.site.urls),
     path('schema/', get_schema_view(title="Fast Food Api", description="API  Description hery", version="1.0.0"),
         name="openapi-schema"),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
