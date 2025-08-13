from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from audioapi.models import BookingStaff, Staff, Booking
from audioapi.serializers import BookingStaffSerializer
import logging

logger = logging.getLogger(__name__)

class BookingStaffView(ViewSet):
    
    def create(self, request):
        try:
            staff = Staff.objects.get(id=request.data['staff_id'])
            
            booking_staff = BookingStaff.objects.create(
                booking_id=request.data['booking_id'],
                staff=staff,
                rate_type=request.data.get('rate_type', 'FULL_DAY'),
                day_rate_at_booking=request.data.get('day_rate_at_booking', staff.day_rate),
                custom_rate=request.data.get('custom_rate'),
                days_worked=request.data.get('days_worked', 1),
                notes=request.data.get('notes', '')
            )
            
            # Update booking total cost
            self.update_booking_cost(booking_staff.booking)
            
            serializer = BookingStaffSerializer(booking_staff)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Staff.DoesNotExist:
            return Response({'error': 'Staff not found'}, status=status.HTTP_404_NOT_FOUND)
        except KeyError as e:
            return Response({'error': f'Missing required field: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f"Error creating booking staff assignment: {str(e)}")
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request):
        try:
            queryset = BookingStaff.objects.select_related('booking', 'staff__user').all()
            
            # Filter by booking
            booking_id = request.query_params.get('booking_id')
            if booking_id:
                queryset = queryset.filter(booking_id=booking_id)
                
            # Filter by staff
            staff_id = request.query_params.get('staff_id')
            if staff_id:
                queryset = queryset.filter(staff_id=staff_id)
            
            assignments = queryset.order_by('-assigned_at')
            serializer = BookingStaffSerializer(assignments, many=True)
            return Response(serializer.data)
        except Exception as e:
            logger.error(f"Error listing booking staff assignments: {str(e)}")
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        try:
            assignment = BookingStaff.objects.select_related('booking', 'staff__user').get(pk=pk)
            serializer = BookingStaffSerializer(assignment)
            return Response(serializer.data)
        except BookingStaff.DoesNotExist:
            return Response({'error': 'Booking staff assignment not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.error(f"Error retrieving booking staff assignment: {str(e)}")
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        try:
            assignment = BookingStaff.objects.get(pk=pk)
            serializer = BookingStaffSerializer(assignment, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                # Update booking total cost
                self.update_booking_cost(assignment.booking)
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except BookingStaff.DoesNotExist:
            return Response({'error': 'Booking staff assignment not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.error(f"Error updating booking staff assignment: {str(e)}")
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, pk=None):
        try:
            assignment = BookingStaff.objects.get(pk=pk)
            serializer = BookingStaffSerializer(assignment, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                # Update booking total cost
                self.update_booking_cost(assignment.booking)
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except BookingStaff.DoesNotExist:
            return Response({'error': 'Booking staff assignment not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.error(f"Error updating booking staff assignment: {str(e)}")
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        try:
            assignment = BookingStaff.objects.get(pk=pk)
            booking = assignment.booking
            assignment.delete()
            # Update booking total cost
            self.update_booking_cost(booking)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except BookingStaff.DoesNotExist:
            return Response({'error': 'Booking staff assignment not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.error(f"Error deleting booking staff assignment: {str(e)}")
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    def update_booking_cost(self, booking):
        """Recalculate and update the total estimated cost"""
        try:
            total_cost = sum(
                assignment.total_cost 
                for assignment in booking.bookingstaff_set.all()
            )
            booking.total_estimated_cost = total_cost
            booking.save(update_fields=['total_estimated_cost'])
        except Exception as e:
            logger.error(f"Error updating booking cost: {str(e)}")