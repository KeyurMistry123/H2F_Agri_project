from django.shortcuts import render

##ngrok run command ------> ngrok http --domain=tightly-daring-killdeer.ngrok-free.app http://127.0.0.1:8000/

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CropRecommendationSerializer
import joblib

import logging

logger = logging.getLogger(__name__)


model = joblib.load(r'C:\Users\hp\H2F_Agri_project\models\crop_recommender.pkl')
class CropRecommendationView(APIView):
    def post(self, request):
        serializer = CropRecommendationSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            features = [
                data['N'], 
                data['P'], 
                data['K'], 
                data['temperature'], 
                data['humidity'], 
                data['ph'], 
                data['rainfall']
            ]
            prediction = model.predict([features])
            return Response({'recommended_crop': prediction[0]}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

