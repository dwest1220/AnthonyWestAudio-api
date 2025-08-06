import datetime
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from audioapi.models import Inquiry
from audioapi.serializers import InquirySerializer

class InquiryView(ViewSet):

    def create(self, request):

        inquiry = Inquiry()
        inquiry.user = request.user
        inquiry.status = request.data['status']
        inquiry.event_name = request.data['event_name']
        inquiry.event_date = request.data['event_date']
        inquiry.location = request.data['location']
        inquiry.message = request.data['message']
        inquiry.created_at = request.data['created_at']
        inquiry.save()

        serialized = InquirySerializer(inquiry, many=False)

        return Response(serialized.data, status=status.HTTP_201_CREATED)
    
