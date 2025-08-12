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
        try:
            inquiry = Inquiry.objects.create(
                user=request.user,
                status=request.data.get('status', 'TENTATIVE'),
                event_name=request.data['event_name'],
                event_date=request.data['event_date'],
                location=request.data['location'],
                phone=request.data['phone'],
                email=request.data['email'],
                message=request.data['message']
            )

            serializer = InquirySerializer(inquiry)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        except KeyError as e:
            return Response({'error': f'Missing required field: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    def list(self, request):
        if request.user.is_staff:
            inquiries = Inquiry.objects.all()
        else:
            inquiries = Inquiry.objects.filter(user=request.user)
        serializer = InquirySerializer(inquiries, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        try:
            if request.user.is_staff:
                inquiry = Inquiry.objects.get(pk=pk)
            else:
                inquiry = Inquiry.objects.get(pk=pk, user=request.user)
            serializer = InquirySerializer(inquiry)
            return Response(serializer.data)
        except Inquiry.DoesNotExist:
            return Response({'error': 'Inquiry not found'}, status=status.HTTP_404_NOT_FOUND)
        
    def update(self, request, pk=None):
        try:
            if request.user.is_staff:
                inquiry = Inquiry.objects.get(pk=pk)
            else:
                inquiry = Inquiry.objects.get(pk=pk, user=request.user)
            serializer = InquirySerializer(inquiry, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Inquiry.DoesNotExist:
            return Response({'error': 'Inquiry not found'}, status=status.HTTP_404_NOT_FOUND)
        
    def partial_update(self, request, pk=None):
        try:
            if request.user.is_staff:
                inquiry = Inquiry.objects.get(pk=pk)
            else:
                inquiry = Inquiry.objects.get(pk=pk, user=request.user)
            serializer = InquirySerializer(inquiry, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Inquiry.DoesNotExist:
            return Response({'error': 'Inquiry not found'}, status=status.HTTP_404_NOT_FOUND)
    
    def destroy(self, request, pk=None):
        """Delete an inquiry"""
        try:
            if request.user.is_staff:
                inquiry = Inquiry.objects.get(pk=pk)
            else:
                inquiry = Inquiry.objects.get(pk=pk, user=request.user)
            inquiry.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Inquiry.DoesNotExist:
            return Response({'error': 'Inquiry not found'}, status=status.HTTP_404_NOT_FOUND)