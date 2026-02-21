from django.contrib import admin
from .models import Profile, Project, WorkExperience, Skill, HomeContent


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """
    Admin configuration for Profile model.
    """
    list_display = ('user', 'phone', 'address', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user__username', 'user__email', 'phone', 'address')
    raw_id_fields = ('user',)
    list_per_page = 25


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    """
    Admin configuration for Project model with slug auto-generation and search/filtering.
    """
    list_display = ('title', 'category', 'featured', 'order', 'created_at', 'updated_at')
    list_filter = ('featured', 'category', 'created_at')
    search_fields = ('title', 'description', 'technologies')
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('featured', 'order')
    ordering = ('order', '-created_at')
    list_per_page = 25
    
    fieldsets = (
        ('Basic Info', {
            'fields': ('title', 'slug', 'description')
        }),
        ('Details', {
            'fields': ('detailed_description', 'image', 'technologies', 'category')
        }),
        ('Links', {
            'fields': ('github_link', 'live_link')
        }),
        ('Display', {
            'fields': ('featured', 'order')
        }),
    )


@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    """
    Admin configuration for WorkExperience model.
    """
    list_display = ('company', 'position', 'start_date', 'end_date', 'is_current', 'is_visible', 'order')
    list_filter = ('is_current', 'is_visible', 'created_at')
    search_fields = ('company', 'position', 'description', 'technologies')
    list_editable = ('is_visible', 'order', 'is_current')
    ordering = ('-is_current', '-start_date', 'order')
    list_per_page = 25
    
    fieldsets = (
        ('Company Info', {
            'fields': ('company', 'position', 'location', 'company_logo')
        }),
        ('Duration', {
            'fields': ('start_date', 'end_date', 'is_current')
        }),
        ('Details', {
            'fields': ('description', 'technologies')
        }),
        ('Display', {
            'fields': ('is_visible', 'order')
        }),
    )


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    """
    Admin configuration for Skill model.
    """
    list_display = ('name', 'category', 'proficiency_level', 'is_visible', 'order')
    list_filter = ('category', 'is_visible')
    search_fields = ('name',)
    list_editable = ('is_visible', 'order', 'proficiency_level')
    ordering = ('category', 'order', 'name')
    list_per_page = 25


@admin.register(HomeContent)
class HomeContentAdmin(admin.ModelAdmin):
    """
    Admin configuration for HomeContent model.
    """
    list_display = ('__str__', 'name', 'is_active', 'created_at', 'updated_at')
    list_filter = ('is_active',)
    list_editable = ('is_active',)
    list_per_page = 25
    
    fieldsets = (
        ('Profile Picture', {
            'fields': ('profile_picture', 'profile_picture_url'),
            'description': 'Upload a profile picture or use an external URL'
        }),
        ('Personal Information', {
            'fields': ('name', 'title', 'education')
        }),
        ('Contact Information', {
            'fields': ('email', 'phone', 'github_url', 'linkedin_url')
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
    )
    
    def has_add_permission(self, request):
        # Only allow one instance
        if HomeContent.objects.exists():
            return False
        return super().has_add_permission(request)
