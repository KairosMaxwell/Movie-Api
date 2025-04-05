from rest_framework import routers
from . import views
from django.urls import path , include

router = routers.DefaultRouter()
router.register("review",views.ReviewViewSet)

urlpattern=[

    path("/api",include(router.urls)),
    path("reviews/", views.ReviewViewSet.as_view(), name="movie-reviews"),
]
