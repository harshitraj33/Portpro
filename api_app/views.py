from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from projects_app.models import Project
from contact_app.models import ContactMessage
from .serializers import ProjectSerializer, ContactMessageSerializer, UserSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]
        return [permissions.IsAdminUser()]
    
    @action(detail=False, methods=['get'])
    def featured(self, request):
        featured_projects = self.queryset.filter(featured=True)
        serializer = self.get_serializer(featured_projects, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def categories(self, request):
        categories = self.queryset.values_list('category', flat=True).distinct()
        return Response(list(categories))


class ContactMessageViewSet(viewsets.ModelViewSet):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer
    
    def get_permissions(self):
        if self.action == 'create':
            return [permissions.AllowAny()]
        return [permissions.IsAdminUser()]
    
    @action(detail=True, methods=['post'])
    def mark_read(self, request, pk=None):
        message = self.get_object()
        message.is_read = True
        message.save()
        serializer = self.get_serializer(message)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'])
    def mark_resolved(self, request, pk=None):
        message = self.get_object()
        message.is_resolved = True
        message.save()
        serializer = self.get_serializer(message)
        return Response(serializer.data)


class AuthViewSet(viewsets.ViewSet):
    @action(detail=False, methods=['post'])
    def login(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            if user.is_active:
                token, _ = Token.objects.get_or_create(user=user)
                serializer = UserSerializer(user)
                return Response({'token': token.key, 'user': serializer.data})
            else:
                return Response({'error': 'Account is disabled'}, status=status.HTTP_403_FORBIDDEN)
        
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    
    @action(detail=False, methods=['post'])
    def register(self, request):
        serializer = UserSerializer(data=request.data)
        
        if serializer.is_valid():
            user = serializer.save()
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['post'])
    def logout(self, request):
        try:
            request.user.auth_token.delete()
            return Response({'message': 'Logout successful'})
        except Exception:
            return Response({'error': 'Logout failed'}, status=status.HTTP_400_BAD_REQUEST)
