from rest_framework import serializers
from . models import sports

# Name the class as (model name + 'Serializer')
class sportsSerializer(serializers.ModelSerializer):
    class Meta:  
        model = sports  
        fields = '__all__'