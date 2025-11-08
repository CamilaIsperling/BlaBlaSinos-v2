from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def ping(request): return JsonResponse({"status": "ok", "api": "BlaBlaSinos v2"})

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/ping/", ping),
    path("api/", include("rides.api.urls")),
]
