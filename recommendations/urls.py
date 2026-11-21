from django.urls import path
from . import views

urlpatterns = [
    # Template views
    path('preferences/', views.preferences_view, name='preferences'),
    path('recommendations/', views.recommendations_view, name='recommendations'),
    path('history/', views.history_view, name='history'),
    path('math-lab/', views.math_lab_view, name='math_lab'),
    
    # API endpoints - Preferences
    path('api/preferences/', views.user_preferences_api, name='api_user_preferences'),
    
    # API endpoints - Recommendations
    path('api/recommendations/', views.generate_recommendations, name='api_generate_recommendations'),
    path('api/recommendations/history/', views.recommendation_history, name='api_recommendation_history'),
    
    # API endpoints - Mathematical Lab
    path('api/math/union/', views.math_operation_union, name='api_math_union'),
    path('api/math/intersection/', views.math_operation_intersection, name='api_math_intersection'),
    path('api/math/difference/', views.math_operation_difference, name='api_math_difference'),
    path('api/math/complement/', views.math_operation_complement, name='api_math_complement'),
    path('api/math/jaccard/', views.math_jaccard_similarity, name='api_math_jaccard'),
    path('api/math/cartesian-product/', views.math_cartesian_product, name='api_math_cartesian'),
    path('api/math/power-set/', views.math_power_set, name='api_math_power_set'),
    path('api/math/verify-de-morgan/', views.math_verify_de_morgan, name='api_math_de_morgan'),
]
