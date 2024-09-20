from django.urls import path
from .views import nutrition_info

urlpatterns = [
    path('nutrition/', nutrition_info),
]
