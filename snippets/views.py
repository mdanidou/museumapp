from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from snippets.models import MUSEUM
from snippets.serializers import SnippetSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from snippets.serializers import UserSerializer
from rest_framework import permissions
from snippets.permissions import IsOwnerOrReadOnly
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend



# @api_view(['GET', 'POST'])
# def museum_list(request, format=None):
#     #List all snippets, or create a new snippet.
#     if request.method == 'GET':
#         snippets = MUSEUM.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def museum_detail(request, pk, format=None):
#     #Retrieve, update or delete a snippet instance.
#     try:
#         snippet = MUSEUM.objects.get(pk=pk)
#     except MUSEUM.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = SnippetSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class museum_list(generics.ListCreateAPIView):
    """
    Returns a list of all snippets.
    For more details on snippets please [see here][ref].
    [ref]: http://example.com/
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = MUSEUM.objects.all()
    serializer_class = SnippetSerializer
    filter_backends = (DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter,)
    # filter_backends = (filters.DjangoFilterBacken, filters.SearchFilter, filters.OrderingFilter,)
    filter_fields = ('NAME','COUNTRY','STATE','CITY','CATEGORYID', 'PRICEID',)
    search_fields = ('$NAME','$COUNTRY','$STATE','$CITY')
    ordering_fields = ('NAME', 'owner')
    ordering = ('NAME',)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class museum_detail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    queryset = MUSEUM.objects.all()
    serializer_class = SnippetSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer