from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from rest_framework import status, generics, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import UserRegistrationSerializer, UserSerializer, UserLoginSerializer


# ========== Template Views ==========

def landing_page(request):
    """Landing page view."""
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'accounts/landing.html')


def login_view(request):
    """Login page view."""
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'accounts/login.html')


def register_view(request):
    """Registration page view."""
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        
        # Basic validation
        if password != password2:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'accounts/register.html')
        
        # Use serializer for validation and creation
        serializer = UserRegistrationSerializer(data={
            'username': username,
            'email': email,
            'password': password,
            'password2': password2,
            'first_name': first_name,
            'last_name': last_name,
        })
        
        if serializer.is_valid():
            user = serializer.save()
            login(request, user)
            messages.success(request, f'Welcome to CineSet, {user.username}!')
            return redirect('dashboard')
        else:
            for field, errors in serializer.errors.items():
                for error in errors:
                    messages.error(request, f'{field}: {error}')
    
    return render(request, 'accounts/register.html')


@login_required
def logout_view(request):
    """Logout view."""
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('landing')


@login_required
def dashboard(request):
    """User dashboard view."""
    return render(request, 'accounts/dashboard.html')


# ========== API Views ==========

@api_view(['POST'])
@permission_classes([AllowAny])
def api_register(request):
    """
    API endpoint for user registration.
    """
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response({
            'message': 'User registered successfully',
            'user': UserSerializer(user).data
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def api_login(request):
    """
    API endpoint for user login.
    """
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({
                'message': 'Login successful',
                'user': UserSerializer(user).data
            }, status=status.HTTP_200_OK)
        return Response({
            'error': 'Invalid credentials'
        }, status=status.HTTP_401_UNAUTHORIZED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def api_logout(request):
    """
    API endpoint for user logout.
    """
    logout(request)
    return Response({
        'message': 'Logout successful'
    }, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_current_user(request):
    """
    API endpoint to get current user information.
    """
    serializer = UserSerializer(request.user)
    return Response(serializer.data)
