from rest_framework import (
    permissions,
    generics,
    response
)
from rest_framework import status, views
from django.shortcuts import get_object_or_404
from rest_framework import filters

from .models import Movie

from . import serializers
from rest_framework import (filters, generics, mixins, permissions, status,
                            viewsets)



class GetModelIdApiView(
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        viewsets.GenericViewSet):
    lookup_field = 'id'
    filter_backends = (filters.SearchFilter,)
    search_fields = ('id',)

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.MovieListSerializer
        return serializers.MovieListSerializer

    def get_serializer_context(self):
        return {
            "request": self.request,
            "args": self.args,
            "kwargs": self.kwargs
        }

    def get_queryset(self):
        queryset = Movie.objects.all()
        chassis_id = self.request.query_params.get('id', None)


        if chassis_id:
            queryset = queryset.filter(id=chassis_id)

        return queryset



class MovieCreateViewSet(
        mixins.CreateModelMixin,
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        mixins.UpdateModelMixin,
        viewsets.GenericViewSet):
    lookup_field = 'id'
    filter_backends = (filters.SearchFilter,)
    search_fields = ('id',)

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.MovieListSerializer
        return serializers.MovieListSerializer

    def get_serializer_context(self):
        return {
            "request": self.request,
            "args": self.args,
            "kwargs": self.kwargs
        }

    def get_queryset(self):
        queryset = Movie.objects.all()


        return queryset