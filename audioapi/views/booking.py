# import datetime
# from rest_framework.viewsets import ViewSet
# from rest_framework.response import Response
# from rest_framework import status
# from django.contrib.auth.models import User
# from audioapi.models import Booking, Inquiry
# from audioapi.serializers import BookingSerializer

# class BookingView(ViewSet):

#     def create(self, request):

#         current_user = User.objects.get(user=request.auth.user)
#         inquiry_id = Inquiry.object.get(pk=request.data['inquiry_id'])

#         booking = Booking()
#         booking.user = current_user
#         booking.inquiry_id = inquiry_id
#         booking.event_date = request.data['event_date']
#         booking.confirmed_by_user = request.data['confirmed_by_user']
#         booking.confirmed_at = request.data['confirmed_at']

#         serialized = BookingSerializer(booking, many=False)

#         return Response(serialized.data, status=status.HTTP_201_CREATED)