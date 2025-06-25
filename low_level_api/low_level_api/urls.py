from django.contrib import admin
from django.urls import path, include
import api.urls
import fbv_api.urls
import cbv_api.urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(api.urls)),
    path("fbv_api", include(fbv_api.urls)),
    path("cbv_api", include(cbv_api.urls)),
]
