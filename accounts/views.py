from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth.models import User
from .models import UserPreference


def register_view(request):
    """User registration view"""
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Create empty preference profile
            UserPreference.objects.create(user=user)
            login(request, user)
            messages.success(request, 'Account created successfully! Please select your genre preferences.')
            return redirect('preferences')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field}: {error}')
    else:
        form = UserCreationForm()
    
    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    """User login view"""
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    """User logout view"""
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('landing')


@login_required
def preferences_view(request):
    """User preferences selection view"""
    # Get or create user preferences
    preferences, created = UserPreference.objects.get_or_create(user=request.user)
    
    # Available genres (should match movie genres)
    available_genres = [
        'Action', 'Adventure', 'Animation', 'Comedy', 'Crime',
        'Documentary', 'Drama', 'Fantasy', 'Horror', 'Mystery',
        'Romance', 'Science Fiction', 'Thriller', 'War', 'Western'
    ]
    
    if request.method == 'POST':
        selected_genres = request.POST.getlist('genres')
        if selected_genres:
            preferences.set_genres_from_list(selected_genres)
            preferences.save()
            messages.success(request, 'Your preferences have been updated!')
            return redirect('recommendations')
        else:
            messages.warning(request, 'Please select at least one genre.')
    
    # Get currently selected genres
    selected_genres = preferences.get_genres_list()
    
    context = {
        'available_genres': available_genres,
        'selected_genres': selected_genres,
        'preferences': preferences,
    }
    
    return render(request, 'accounts/preferences.html', context)
