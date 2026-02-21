from rest_framework import serializers
from projects_app.models import Project, Profile
from contact_app.models import ContactMessage
from accounts_app.models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'bio', 'profile_picture', 
                  'website', 'github', 'linkedin', 'twitter', 'created_at']
        read_only_fields = ['id', 'created_at']


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Profile
        fields = ['id', 'user', 'bio', 'profile_picture', 'phone', 'address', 'skills', 
                  'resume', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class ProjectSerializer(serializers.ModelSerializer):
    technologies_list = serializers.SerializerMethodField()
    
    class Meta:
        model = Project
        fields = ['id', 'title', 'slug', 'description', 'detailed_description', 'image',
                  'github_link', 'live_link', 'technologies', 'technologies_list', 
                  'category', 'featured', 'order', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def get_technologies_list(self, obj):
        return obj.get_technologies_list()


class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = ['id', 'name', 'email', 'subject', 'message', 'is_read', 
                  'is_resolved', 'created_at', 'updated_at']
        read_only_fields = ['id', 'is_read', 'is_resolved', 'created_at', 'updated_at']
