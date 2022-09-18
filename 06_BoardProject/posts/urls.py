from rest_framework import routers
from posts.views import PostViewSet

router = routers.SimpleRouter()
router.register('posts', PostViewSet)

urlpatterns = router.urls
