from rest_framework import serializers

class CropRecommendationSerializer(serializers.Serializer):
    N = serializers.IntegerField()
    P = serializers.IntegerField()
    K = serializers.IntegerField()
    temperature = serializers.FloatField()
    humidity = serializers.FloatField()
    ph = serializers.FloatField()
    rainfall = serializers.FloatField()
