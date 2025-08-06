from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from audioapi.models import *
from audioapi.views import *

router = routers.DefaultRouter(trailing_slash=False)
router.register(r"inquiries", InquiryView, basename="inquiry")

urlpatterns = [
    path('', include(router.urls)),
]

