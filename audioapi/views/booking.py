from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from audioapi.models import Booking
from audioapi.serializers import BookingSerializer
import logging

logger = logging.getLogger(__name__)

class BookingView(ViewSet):
    
    def create(self, request):
        try:
            booking = Booking.objects.create(
                inquiry_id=request.data['inquiry_id'],
                booking_date=request.data['booking_date'],
                end_date=request.data.get('end_date'),
                status=request.data.get('status', 'CONFIRMED'),
                contact_phone=request.data.get('contact_phone'),
                contact_email=request.data.get('contact_email'),
                total_estimated_cost=request.data.get('total_estimated_cost'),
                notes=request.data.get('notes', '')
            )
            serializer = BookingSerializer(booking)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except KeyError as e:
            return Response({'error': f'Missing required field: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f"Error creating booking: {str(e)}")
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request):
        try:
            queryset = Booking.objects.select_related('inquiry').all()
            
            # Filter by status
            status_filter = request.query_params.get('status')
            if status_filter:
                queryset = queryset.filter(status=status_filter)
            
            # Filter by date range
            start_date = request.query_params.get('start_date')
            end_date = request.query_params.get('end_date')
            if start_date:
                queryset = queryset.filter(booking_date__gte=start_date)
            if end_date:
                queryset = queryset.filter(booking_date__lte=end_date)
            
            bookings = queryset.order_by('-booking_date')
            serializer = BookingSerializer(bookings, many=True)
            return Response(serializer.data)
        except Exception as e:
            logger.error(f"Error listing bookings: {str(e)}")
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        try:
            booking = Booking.objects.select_related('inquiry').get(pk=pk)
            serializer = BookingSerializer(booking)
            return Response(serializer.data)
        except Booking.DoesNotExist:
            return Response({'error': 'Booking not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.error(f"Error retrieving booking: {str(e)}")
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        try:
            booking = Booking.objects.get(pk=pk)
            serializer = BookingSerializer(booking, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Booking.DoesNotExist:
            return Response({'error': 'Booking not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.error(f"Error updating booking: {str(e)}")
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, pk=None):
        try:
            booking = Booking.objects.get(pk=pk)
            serializer = BookingSerializer(booking, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Booking.DoesNotExist:
            return Response({'error': 'Booking not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.error(f"Error updating booking: {str(e)}")
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        try:
            booking = Booking.objects.get(pk=pk)
            booking.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Booking.DoesNotExist:
            return Response({'error': 'Booking not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.error(f"Error deleting booking: {str(e)}")
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)