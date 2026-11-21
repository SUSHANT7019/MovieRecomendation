"""
URL configuration for movie project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from accounts import views as accounts_views
from movies import views as movies_views
from recommendations import views as recommendations_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Landing page
    path('', recommendations_views.landing_view, name='landing'),
    
    # Authentication
    path('accounts/register/', accounts_views.register_view, name='register'),
    path('accounts/login/', accounts_views.login_view, name='login'),
    path('accounts/logout/', accounts_views.logout_view, name='logout'),
    path('accounts/preferences/', accounts_views.preferences_view, name='preferences'),
    
    # Movies
    path('movies/', movies_views.movie_explorer_view, name='movie_explorer'),
    path('movies/<int:movie_id>/', movies_views.movie_detail_view, name='movie_detail'),
    
    # Recommendations
    path('recommendations/', recommendations_views.recommendations_view, name='recommendations'),
    path('recommendations/math-lab/', recommendations_views.math_lab_view, name='math_lab'),
    path('api/math-lab/', recommendations_views.math_lab_api_view, name='math_lab_api'),
    path('dashboard/', recommendations_views.dashboard_view, name='dashboard'),
    
    # Favorites
    path('favorites/add/<int:movie_id>/', recommendations_views.add_favorite_view, name='add_favorite'),
    path('favorites/remove/<int:movie_id>/', recommendations_views.remove_favorite_view, name='remove_favorite'),
]

