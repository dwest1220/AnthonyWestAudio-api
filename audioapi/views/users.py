from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class UserView(ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        if not request.user.is_staff:
            return Response({'error': 'Admin access is required'}, status=status.HTTP_403_FORBIDDEN)
        
        users = User.objects.all()
        user_data = [{
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'is_staff': user.is_staff,
            'is_active': user.is_active,
        } for user in users]

        return Response(user_data)

    def create(self, request):
        if not request.user.is_staff:
            return Response({'error': 'Admin access is required'}, status=status.HTTP_403_FORBIDDEN)
         
        try:
            user = User.objects.create(
                username=request.data['username'],
                email=request.data.get('email', ''),
                first_name=request.data.get('first_name', ''),
                last_name=request.data.get('last_name', ''),
                password=make_password(request.data['password']),
                is_staff=request.data.get('is_staff', False),
                is_active=request.data.get('is_active', True)
            )

            return Response({
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'message': 'User created successfully'
            }, status=status.HTTP_201_CREATED)
        
        except KeyError as e:
            return Response({'error': f'Missing required field: {e}'})
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    def retrieve(self, request, pk=None):

        try:
            if pk != str(request.user.id) and not  request.user.is_staff:
                return Response({'error': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)
            
            user = User.objects.get(pk=pk)

            user.email = request.data.get('email', user.email)
            user.first_name = request.data.get('first_name', user.first_name)
            user.last_name = request.data.get('last_name', user.last_name)

            if request.user.is_staff:
                user.is_staff = request.data.get('is_staff', user.is_staff)
                user.is_active = request.data.get('is_active', user.is_active)
            
            if 'password' in request.data:
                user.set_password(request.data['password'])
            
            user.save()

            return Response({
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'message': 'User updated successfully'
            })
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        """Delete a user (admin only)"""
        if not request.user.is_staff:
            return Response({'error': 'Admin access required'}, status=status.HTTP_403_FORBIDDEN)
        
        # Prevent self-deletion
        if pk == str(request.user.id):
            return Response({'error': 'Cannot delete your own account'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            user = User.objects.get(pk=pk)
            username = user.username
            user.delete()
            
            return Response({'message': f'User {username} deleted successfully'})
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)