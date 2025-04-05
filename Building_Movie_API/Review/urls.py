# from rest_framework import routers
# from . import views
# from django.urls import path , include
#
# router = routers.DefaultRouter()
# router.register("review",views.ReviewViewSet)
#
# urlpattern=[
#
#     path("/api",include(router.urls)),
#     path("reviews/", views.ReviewViewSet.as_view(), name="movie-reviews"),
# ]



from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReviewViewSet

router = DefaultRouter()
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
