from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("recruitment/", include('recruitmentapi.urls')),
    path('admin/', admin.site.urls),
]
