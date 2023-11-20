from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("recriutment/", include('recruitmentapi.urls')),
    path('admin/', admin.site.urls),
]
