from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import CommentViewSet, FollowingViewSet, GroupViewSet, PostViewSet

router = SimpleRouter()
router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)
router.register(
    r'^posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comment'
)


urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
    path('', include(router.urls)),
    path(
        'follow/',
        FollowingViewSet.as_view({'get': 'list', 'post': 'create'})
    ),
]
