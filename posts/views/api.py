from rest_framework import  generics
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from posts.models import Post
from posts.serializers import PostSerializer


class PostsPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 1000


class PostListAPI(generics.ListAPIView):
    lookup_field =  'pk'
    serializer_class =  PostSerializer
    pagination_class = PostsPagination
    #queryset =      Post.objects.all()
    def get_queryset(self):
        return Post.objects.all()


class PostCreateAPI(generics.CreateAPIView):
    lookup_field = 'pk'
    serializer_class = PostSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Post.objects.all()