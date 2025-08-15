from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from audioapi.views.auth import login_view, logout_view, user_profile_view
from audioapi.models import *
from audioapi.views import *

router = routers.DefaultRouter(trailing_slash=False)
router.register(r"inquiries", InquiryView, basename="inquiry")
router.register(r"users", UserView, basename="user")
router.register(r'staff', StaffView, basename='staff')
router.register(r'bookings', BookingView, basename='booking')
router.register(r'booking-staff', BookingStaffView, basename='booking-staff')

urlpatterns = [
    path('auth/register/', register_view, name='register'),
    path('auth/login/', login_view, name='login'),
    path('auth/logout/', logout_view, name='logout'),
    path('auth/user/', user_profile_view, name='user-profile'),
    path('', include(router.urls)),
]

