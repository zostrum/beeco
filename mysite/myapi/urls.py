from django.conf.urls import include, url
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'reader_book', views.reader_bookViewSet)
router.register(r'publish_houses', views.publish_houseViewSet)
router.register(r'books', views.bookViewSet)
router.register(r'comments', views.commentViewSet)
router.register(r'genres', views.genreViewSet)
router.register(r'authors', views.authorViewSet)
router.register(r'country', views.countryViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]