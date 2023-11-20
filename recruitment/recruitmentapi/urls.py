from django.urls import path
from .views import *

urlpatterns = [
    path('sample', sample.as_view(), name="recruitment form"),
    path('submit', recruitmentFormData.as_view(), name="recruitment form"),
]
