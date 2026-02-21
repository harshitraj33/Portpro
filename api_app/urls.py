from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'api'

router = DefaultRouter()
router.register(r'projects', views.ProjectViewSet, basename='project')
router.register(r'contact', views.ContactMessageViewSet, basename='contact')
router.register(r'auth', views.AuthViewSet, basename='auth')

urlpatterns = [
    path('', include(router.urls)),
]
