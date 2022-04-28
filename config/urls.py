from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import GoogleLogin
from rest_framework.schemas import get_schema_view
from drf_yasg.views import get_schema_view as doc_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny


schema_view = doc_schema_view(
    openapi.Info(
        title="News API",
        default_version="v1",
        description="Bu API sizga yangiliklar taqdim etadi!",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="bekzod030900@gmail.com"),
        license=openapi.License(name="DATA UNION MCHJ")
    ),
    public=True,
    permission_classes=(AllowAny, )
)


urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('api/v1/', include('api.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
    path('captcha/', include('captcha.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/dj-rest-auth/', include('dj_rest_auth.urls')),
    path('api/v1/dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('api/v1/dj-rest-auth/google/', GoogleLogin.as_view(), name='google_login'),
    path('accounts/', include('allauth.urls')),
    path('openapi/', get_schema_view(
        title="News API",
        description="Bu API sizga yangiliklar taqdim etadi!",
        version="1.0.0"
    ), name="open-api"),
    path('swagger/', schema_view.with_ui(
        'swagger', cache_timeout=0), name="schema-swagger-ui"),
    path('redoc/', schema_view.with_ui(
        'redoc', cache_timeout=0), name="schema-redoc")
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
