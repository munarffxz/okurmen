# course/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MasterClassViewSet, TechnologyViewSet, CourseViewSet, create_course

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'technologies', TechnologyViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'masterclasses', MasterClassViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('courses/create/', create_course, name='course-create'),
]
