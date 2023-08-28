from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view (
   openapi.Info(
      title="Health and Fitness API",
      default_version='v1',
      description="The Health and Fitness API provides endpoints to "
      "track workouts, set goals, monitor progress, and manage health-related data. ",
      contact=openapi.Contact(email="fitlife@gmail.com"),
      
   ),
   public=True,
   permission_classes=(permissions.AllowAny,)
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    path('api/',include('api.urls')),
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]
