from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from django.contrib import admin
from django.urls import path

static_urls = static(settings.MEDIA_URL, document_root=settings.MEDIAL_ROOT)

urlpatterns = [
    path("supersecret/", admin.site.urls),
] + static_urls

