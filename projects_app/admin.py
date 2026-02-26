from django.contrib import admin
from .models import Profile, Project, WorkExperience, Skill, HomeContent, AboutContent


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


@admin.register(AboutContent)
class AboutContentAdmin(admin.ModelAdmin):
    """
    Admin configuration for AboutContent model.
    """
    list_display = ('__str__', 'is_active', 'created_at', 'updated_at')
    list_filter = ('is_active',)
    list_editable = ('is_active',)
    list_per_page = 25
    
    fieldsets = (
        ('Bio / Introduction', {
            'fields': ('bio',),
            'description': 'Main introduction text for the about page'
        }),
        ('Skills - Programming Languages', {
            'fields': ('skills_languages',),
            'description': 'Comma-separated list of programming languages (e.g., Python, Java, C++)'
        }),
        ('Skills - Frameworks', {
            'fields': ('skills_frameworks',),
            'description': 'Comma-separated list of frameworks (e.g., React, Django)'
        }),
        ('Skills - Tools & Platforms', {
            'fields': ('skills_tools',),
            'description': 'Comma-separated list of tools and platforms (e.g., MySQL, Git, AWS)'
        }),
        ('Skills - Soft Skills', {
            'fields': ('skills_soft',),
            'description': 'Comma-separated list of soft skills (e.g., Creative, Problem Solver)'
        }),
        ('Internship 1', {
            'fields': ('internship_1_company', 'internship_1_position', 'internship_1_date', 'internship_1_description', 'internship_1_tech'),
            'description': 'First internship entry'
        }),
        ('Internship 2', {
            'fields': ('internship_2_company', 'internship_2_position', 'internship_2_date', 'internship_2_description', 'internship_2_tech'),
            'description': 'Second internship entry'
        }),
        ('Certificates', {
            'fields': ('certificates',),
            'description': 'One certificate per line'
        }),
        ('Education 1 (Latest)', {
            'fields': ('education_1_institution', 'education_1_degree', 'education_1_date', 'education_1_cgpa', 'education_1_location'),
            'description': 'First education entry (usually latest/bachelor)'
        }),
        ('Education 2 (Previous)', {
            'fields': ('education_2_institution', 'education_2_degree', 'education_2_date', 'education_2_cgpa', 'education_2_location'),
            'description': 'Second education entry (usually diploma/school)'
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
    )
    
    def has_add_permission(self, request):
        # Only allow one instance
        if AboutContent.objects.exists():
            return False
        return super().has_add_permission(request)
