# class museum_list(generics.ListCreateAPIView):
#     """
#     Returns a list of all snippets.
#     For more details on snippets please [see here][ref].
#     [ref]: http://example.com/
#     """
#     # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#     queryset = MUSEUM.objects.all()
#     serializer_class = SnippetSerializer
#     # filter_backends = (filters.DjangoFilterBacken,filters.SearchFilter, filters.OrderingFilter,)
#     # filter_fields = ('title', 'code', 'linenos', 'owner')
#     # search_fields = ('title', 'code')
#     # ordering_fields = ('title', 'owner')
#     #
#     # def perform_create(self, serializer):
#     #     serializer.save(owner=self.request.user)
#
#
# class museum_detail(generics.RetrieveUpdateDestroyAPIView):
#     # permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
#     queryset = MUSEUM.objects.all()
#     serializer_class = SnippetSerializer