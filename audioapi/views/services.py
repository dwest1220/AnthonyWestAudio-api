from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from audioapi.models import Service
from audioapi.serializers import ServiceSerializer
import logging

logger = logging.getLogger(__name__)

class ServiceView(ViewSet):

    def create(self, request):
        try:
            service = Service.objects.create(
                name=request.data['name'],
                description=request.data['description'],
                details=request.data['details'],
                price=request.data['price']
            )

            serializer = ServiceSerializer(service)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        except KeyError as e:
            return Response({'error': f'Missing required field: {str(e)}'})
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    def list(self, request):
        try:
            service = Service.objects.all()
            
            serializer = ServiceSerializer(service, many=True)
            return Response(serializer.data)
        
        except Exception as e:
            logger.error(f"Error returning services: {str(e)}")
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    def retrieve(self, request, pk=None):
        try:
            service = get_object_or_404(Service, pk=pk)
            serializer = ServiceSerializer(service)
            return Response(serializer.data)
        
        except Exception as e:
            logger.error(f"Error retrieving service {pk}: {str(e)}")
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request, pk=None):
        try:
            service = get_object_or_404(Service, pk=pk)
            service.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            logger.error(f"Error deleting service {pk}: {str(e)}")
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        