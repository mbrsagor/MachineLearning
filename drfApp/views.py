from django.shortcuts import render, get_object_or_404
from .models import (
    Post,
    Category
)
from .serializers import (
    PostSeiralizer,
    CategorytSeiralizer
)
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.permissions import IsAuthenticated



class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSeiralizer
    # permission_classes = (IsAuthenticated,)



class CategoryAPIView(APIView):
    # permission_classes = (IsAuthenticated,)
    def get(self, request):
        category = Category.objects.all()
        serializer = CategorytSeiralizer(category, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorytSeiralizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class DeleteCategory(APIView):
    # permission_classes = (IsAuthenticated,)
    def get(self, request, pk):
        category   = get_object_or_404(Category, pk=pk)
        serializer = CategorytSeiralizer(category).data
        return Response(serializer)

    def put(self, request, pk):
        cat = get_object_or_404(Category, pk=pk)
        serializer = CategorytSeiralizer(cat, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
