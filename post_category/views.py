
from post_category.models import PostCategory
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view

from post_category.serializers import PostCategorySerializer


@api_view(['GET', 'POST'])
def categories_list(request):
    if request.method == 'GET':
        categories = PostCategory.objects.all()
        serializer = PostCategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = PostCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def categories_detail(request, pk):
    try:
        category = PostCategory.objects.get(pk=pk)
    except PostCategory.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = PostCategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'PUT':
        serializer = PostCategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
    if request.method == 'PATCH':
        serializer = PostCategorySerializer(category, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
    if request.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
