from django.urls import path, include
from .views import api as views


posts_api_urlpatterns = ([

        path('', views.PostListAPI.as_view(), name='list'),
        path('create/', views.PostCreateAPI.as_view(), name='create'),

], 'posts-api')


urlpatterns = [
    path('', include(posts_api_urlpatterns))
]