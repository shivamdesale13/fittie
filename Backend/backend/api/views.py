from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def nutrition_info(request):
    data = {
        'calories': 2000,
        'carbs': 250,
        'protein': 50,
        'fat': 70
    }
    return Response(data)



