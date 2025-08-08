from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.decorators import authentication_classes



@api_view(['POST'])
@permission_classes([AllowAny])  # Allow anyone to login
@authentication_classes([])  # Don't require auth for login
def login_view(request):
    print(f"Login attempt - Data received: {request.data}")

    username = request.data.get('username')
    password = request.data.get('password')

    print(f"Username: {username}, Password: {'*' * len(password) if password else None}")
    
    if not username or not password:
        return Response(
            {'error': 'Username and password are required'}, 
            status=status.HTTP_400_BAD_REQUEST
        )
    
    user = authenticate(username=username, password=password)
    print(f"Authentication result: {user}")
    
    if user:
        token, created = Token.objects.get_or_create(user=user)
        print(f"Token created/retrieved: {token.key[:10]}... (created: {created})")
        return Response({
            'token': token.key,
            'user': {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name,
            }
        }, status=status.HTTP_200_OK)
    else:
        return Response(
            {'error': 'Invalid credentials'}, 
            status=status.HTTP_401_UNAUTHORIZED
        )

@api_view(['POST'])
def logout_view(request):
    try:
        # Delete the user's token to logout
        request.user.auth_token.delete()
        return Response({'message': 'Successfully logged out'}, status=status.HTTP_200_OK)
    except:
        return Response({'error': 'Error logging out'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def user_profile_view(request):
    """Get current user's profile"""
    user = request.user
    return Response({
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name,
    })