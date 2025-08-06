import datetime
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from audioapi.models import Inquiry
from audioapi.serializers import InquirySerializer
import logging

logger = logging.getLogger(__name__)

class InquiryView(ViewSet):

    def create(self, request):

        # inquiry = Inquiry()
        # inquiry.user = request.user
        # inquiry.status = request.data['status']
        # inquiry.event_name = request.data['event_name']
        # inquiry.event_date = request.data['event_date']
        # inquiry.location = request.data['location']
        # inquiry.message = request.data['message']
        # inquiry.created_at = request.data['created_at']
        # inquiry.save()

        # serialized = InquirySerializer(inquiry, many=False)

        # return Response(serialized.data, status=status.HTTP_201_CREATED)

        logger.info(f"InquiryView.create called by user: {request.user}")
        print(f"DEBUG: InquiryView.create called with data {request.data}")

        try:
            inquiry = Inquiry.objects.create(
                user=request.user,
                status=request.data.get('status', 'TENTATIVE'),
                event_name=request.data['event_name'],
                event_date=request.data['event_date'],
                location=request.data['location'],
                message=request.data['message']
            )

            serializer = InquirySerializer(inquiry)
            print(f"DEBUG: Successfully created inquiry with ID: {inquiry.id}")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        except KeyError as e:
            return Response({'error': f'Missing required field: {str(e)}'})
        except Exception as e:
            print(f"DEBUG: Error creating inquiry: {str(e)}")
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    def list(self, request):
        inquiries = Inquiry.objects.filter(user=request.user)
        serializer = InquirySerializer(inquiries, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):

        try:
            inquiry = inquiry.objects.get(pk=pk, user=request.user)
            serializer = InquirySerializer(inquiry)
            return Response(serializer.data)
        except Inquiry.DoesNotExist:
            return Response({'error': 'Inquiry not found'}, status=status.HTTP_404_NOT_FOUND)
        
    def update(self, request, pk=None):

        try:
            inquiry = Inquiry.objects.get(pk=pk, user=request.user)
            serializer = InquirySerializer(inquiry, data=request, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Inquiry.DoesNotExist:
            return Response({'error': 'Inquiry not found'}, status=status.HTTP_404_NOT_FOUND)
    
    def destroy(self, request, pk=None):
        """Delete an inquiry"""
        try:
            inquiry = Inquiry.objects.get(pk=pk, user=request.user)
            inquiry.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Inquiry.DoesNotExist:
            return Response({'error': 'Inquiry not found'}, status=status.HTTP_404_NOT_FOUND)
    
