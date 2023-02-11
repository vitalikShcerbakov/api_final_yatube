from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet ,GroupViewSet, PostViewSet, FollowViewSet

router = DefaultRouter()
router.register('groups', GroupViewSet)
router.register('posts', PostViewSet)
router.register('follow', FollowViewSet, basename='follow')
router.register(r'posts/(?P<id>\d+)/comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('v1/', include(router.urls)),
    # Djoser создаст набор необходимых эндпоинтов.
    # базовые, для управления пользователями в Django:
    path('auth/', include('djoser.urls')),
    # JWT-эндпоинты, для управления JWT-токенами:
    path('v1/', include('djoser.urls.jwt')),
]
