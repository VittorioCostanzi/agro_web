from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('agro-web/', include('agro_web_app.urls')),
]
