# from django.shortcuts import render
# from django.urls import path , include
# from rest_framework import viewsets, permissions
#
# from Review.models import Review
# from Review.serializer import ReviewSerializer
#
#
# from rest_framework.generics import ListAPIView
# from rest_framework.filters import OrderingFilter
# from django_filters.rest_framework import DjangoFilterBackend
#
# class IsOwnerOrReadOnly(permissions.BasePermission):
#     def has_object_permission(self,request,view,obj):
#         if request.method in permissions.SAFE_METHODS:
#             return True
#         return obj.user == request.user
#
#
#
# class ReviewViewSet(viewsets.ModelViewSet):
#     serializer_class = ReviewSerializer
#     queryset = Review.objects.all().order_by("created_Date")
#     filter_backends = [DjangoFilterBackend, OrderingFilter]
#     filterset_fields = ["movie__title"]  # Filter by Movie Title
#     permission_class = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
#     ordering_fields = ["rating", "created_at"]
#
#     def perform_review(self,serializer):
#         serializer.save(user = self.request.user)
#
#


from rest_framework import viewsets, permissions
from .models import Review
from serializer import ReviewSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all().order_by('-created_at')
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]  # Require authentication

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

