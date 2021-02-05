from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Movie


class MovieListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = ['id','movie_name','artist','album','movie_name']

