from django.contrib import admin
from django.contrib.admin import AdminSite
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe

from .models import CustomUser


# Extend Django's default admin site to add custom CSS
class MyAdminSite(AdminSite):
    """Custom Admin Site with theme styling added to default admin"""
    
    def each_context(self, request):
        context = super().each_context(request)
        # Add custom CSS to every admin page
        css = '''
            <style>
                /* Import Orbitron Font */
                @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&display=swap');
                
                :root {
                    --poi-black: #0a0a0a;
                    --poi-dark: #0d1117;
                    --poi-blue: #00a8e8;
                    --poi-white: #ffffff;
                    --poi-gray: #1a1a1a;
                    --poi-border: #333;
                }
                
                /* Body & Base Styles */
                body {
                    background-color: var(--poi-black) !important;
                    color: #e5e7eb !important;
                    font-family: 'Orbitron', 'Courier New', monospace !important;
                }
                
                /* Header */
                #header {
                    background: var(--poi-dark) !important;
                    border-bottom: 1px solid var(--poi-border) !important;
                }
                
                #header a.brand {
                    color: var(--poi-blue) !important;
                    text-shadow: 0 0 5px var(--poi-blue) !important;
                }
                
                /* Sidebar */
                #nav-sidebar {
                    background: var(--poi-dark) !important;
                    border-right: 1px solid var(--poi-border) !important;
                }
                
                #nav-sidebar a {
                    color: #9ca3af !important;
                }
                
                #nav-sidebar a:hover {
                    background-color: #1a1a1a !important;
                    color: var(--poi-blue) !important;
                }
                
                #nav-sidebar a.selected {
                    background-color: rgba(0, 168, 232, 0.1) !important;
                    color: var(--poi-blue) !important;
                    border-left: 2px solid var(--poi-blue) !important;
                }
                
                /* Module / Card Styles */
                .module {
                    background: var(--poi-dark) !important;
                    border: 1px solid var(--poi-border) !important;
                    border-radius: 8px !important;
                    box-shadow: 0 0 5px rgba(0, 168, 232, 0.1) !important;
                }
                
                .module h2, .module h3 {
                    background: var(--poi-gray) !important;
                    color: var(--poi-blue) !important;
                    border-bottom: 1px solid var(--poi-border) !important;
                }
                
                /* Table Styles */
                .results table {
                    background: var(--poi-dark) !important;
                }
                
                .results th {
                    background: var(--poi-gray) !important;
                    color: var(--poi-blue) !important;
                    border-bottom: 1px solid var(--poi-border) !important;
                }
                
                .results td {
                    border-bottom: 1px solid var(--poi-border) !important;
                    color: #e5e7eb !important;
                }
                
                .results tr:hover {
                    background: rgba(0, 168, 232, 0.05) !important;
                }
                
                /* Form Styles */
                input[type="text"],
                input[type="password"],
                input[type="email"],
                input[type="url"],
                input[type="number"],
                textarea,
                select {
                    background: var(--poi-black) !important;
                    border: 1px solid var(--poi-border) !important;
                    color: var(--poi-blue) !important;
                    border-radius: 4px !important;
                }
                
                input:focus, textarea:focus, select:focus {
                    border-color: var(--poi-blue) !important;
                    box-shadow: 0 0 5px var(--poi-blue) !important;
                    outline: none !important;
                }
                
                /* Labels */
                label {
                    color: var(--poi-blue) !important;
                }
                
                /* Buttons */
                .button, input[type="submit"], .submit-row input {
                    background: transparent !important;
                    border: 1px solid var(--poi-blue) !important;
                    color: var(--poi-blue) !important;
                    border-radius: 4px !important;
                }
                
                .button:hover, input[type="submit"]:hover, .submit-row input:hover {
                    background: var(--poi-blue) !important;
                    color: var(--poi-black) !important;
                    box-shadow: 0 0 15px var(--poi-blue) !important;
                }
                
                .button.default, input[type="submit"].default {
                    background: var(--poi-blue) !important;
                    color: var(--poi-black) !important;
                }
                
                /* Links */
                a {
                    color: var(--poi-blue) !important;
                }
                
                a:hover {
                    color: #00c8ff !important;
                }
                
                /* Breadcrumbs */
                .breadcrumbs {
                    background: var(--poi-gray) !important;
                    color: #9ca3af !important;
                }
                
                /* Pagination */
                .paginator {
                    background: var(--poi-gray) !important;
                    border-top: 1px solid var(--poi-border) !important;
                }
                
                .paginator a, .paginator span {
                    border: 1px solid var(--poi-border) !important;
                    color: #9ca3af !important;
                }
                
                .paginator a:hover {
                    border-color: var(--poi-blue) !important;
                    color: var(--poi-blue) !important;
                }
                
                /* Filter Sidebar */
                #changelist-filter {
                    background: var(--poi-gray) !important;
                    border-left: 1px solid var(--poi-border) !important;
                }
                
                #changelist-filter h3 {
                    color: var(--poi-blue) !important;
                }
                
                #changelist-filter li a {
                    color: #9ca3af !important;
                }
                
                #changelist-filter li.selected a {
                    color: var(--poi-blue) !important;
                }
                
                /* Toolbar */
                #toolbar {
                    background: var(--poi-gray) !important;
                    border-bottom: 1px solid var(--poi-border) !important;
                }
                
                #searchbar {
                    background: var(--poi-black) !important;
                    border: 1px solid var(--poi-border) !important;
                    color: var(--poi-blue) !important;
                }
                
                /* Actions */
                .actions {
                    background: var(--poi-gray) !important;
                    border-bottom: 1px solid var(--poi-border) !important;
                }
                
                .actions select {
                    background: var(--poi-black) !important;
                    border: 1px solid var(--poi-border) !important;
                    color: var(--poi-blue) !important;
                }
                
                /* Messages */
                .messagelist .success {
                    background: rgba(34, 197, 94, 0.1) !important;
                    border: 1px solid #22c55e !important;
                    color: #22c55e !important;
                }
                
                .messagelist .error {
                    background: rgba(239, 68, 68, 0.1) !important;
                    border: 1px solid #ef4444 !important;
                    color: #ef4444 !important;
                }
                
                /* Delete confirmation */
                .delete-confirmation {
                    background: var(--poi-dark) !important;
                    border: 1px solid var(--poi-border) !important;
                }
                
                /* Date hierarchy */
                .date-hierarchy {
                    background: var(--poi-gray) !important;
                }
                
                /* Login page specific */
                .login #header {
                    display: none !important;
                }
                
                .login #container {
                    background: var(--poi-black) !important;
                }
                
                /* Selector */
                select {
                    background: var(--poi-black) !important;
                    border: 1px solid var(--poi-border) !important;
                    color: var(--poi-blue) !important;
                }
                
                /* Checkbox */
                input[type="checkbox"] {
                    accent-color: var(--poi-blue) !important;
                }
                
                /* Calendar & DateTime */
                .calendarbox, .clockbox {
                    background: var(--poi-dark) !important;
                    border: 1px solid var(--poi-border) !important;
                }
                
                .calendarbox a, .clockbox a {
                    color: var(--poi-blue) !important;
                }
                
                /* Admin password change form */
                .password_change_form {
                    background: var(--poi-dark) !important;
                }
                
                /* Inline groups */
                .inline-group {
                    background: var(--poi-dark) !important;
                    border: 1px solid var(--poi-border) !important;
                }
                
                /* Object tools */
                .object-tools a {
                    background: transparent !important;
                    border: 1px solid var(--poi-blue) !important;
                    color: var(--poi-blue) !important;
                }
                
                .object-tools a:hover {
                    background: var(--poi-blue) !important;
                    color: var(--poi-black) !important;
                }
                
                /* Scrollbar styling for webkit */
                ::-webkit-scrollbar {
                    width: 8px;
                    height: 8px;
                }
                
                ::-webkit-scrollbar-track {
                    background: var(--poi-black) !important;
                }
                
                ::-webkit-scrollbar-thumb {
                    background: var(--poi-border) !important;
                    border-radius: 4px;
                }
                
                ::-webkit-scrollbar-thumb:hover {
                    background: var(--poi-blue) !important;
                }
                
                /* Hide theme toggle button in Django admin */
                #theme-toggle-container,
                .theme-toggle,
                [id*="theme-toggle"],
                [class*="theme-toggle"],
                .django-admin-assets,
                [data-theme-toggle],
                .flex.items-center.gap-2,
                button[aria-label*="theme"],
                button[title*="theme"] {
                    display: none !important;
                    visibility: hidden !important;
                    opacity: 0 !important;
                }
            </style>
        '''
        context['extra_css'] = mark_safe(css)
        return context


# Create custom admin site instance
my_admin_site = MyAdminSite(name='admin')

# Replace Django's default admin site with our custom one
# This must be done BEFORE any registrations
admin.site = my_admin_site


# =============================================================================
# CustomUser Admin
# =============================================================================
class CustomUserAdmin(UserAdmin):
    """Admin configuration for CustomUser model."""
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_superuser', 'is_active')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)
    
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {
            'fields': ('bio', 'profile_picture', 'website', 'github', 'linkedin', 'twitter')
        }),
    )
    
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {
            'fields': ('bio', 'profile_picture', 'website', 'github', 'linkedin', 'twitter')
        }),
    )


# =============================================================================
# Projects App Admin Configurations
# =============================================================================
from django import forms
from projects_app.models import Profile, Project, WorkExperience, Skill, HomeContent, AboutContent, VisitCount


class ProjectForm(forms.ModelForm):
    """Custom form for Project model with enhanced date input widget."""
    class Meta:
        model = Project
        fields = '__all__'
        widgets = {
            'created': forms.DateInput(attrs={'type': 'date', 'class': 'vDateField'}, format='%Y-%m-%d'),
            'start_date': forms.DateInput(attrs={'type': 'date', 'class': 'vDateField'}, format='%Y-%m-%d'),
            'end_date': forms.DateInput(attrs={'type': 'date', 'class': 'vDateField'}, format='%Y-%m-%d'),
        }


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'address', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user__username', 'user__email', 'phone', 'address')
    raw_id_fields = ('user',)
    list_per_page = 25


class ProjectAdmin(admin.ModelAdmin):
    form = ProjectForm
    list_display = ('title', 'category', 'featured', 'order', 'created', 'created_at', 'updated_at')
    list_filter = ('featured', 'category', 'created_at')
    search_fields = ('title', 'description', 'technologies')
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('featured', 'order')
    ordering = ('order', '-created_at')
    list_per_page = 25
    
    fieldsets = (
        ('Basic Info', {
            'fields': ('title', 'slug', 'description', 'created')
        }),
        ('Project Duration', {
            'fields': ('start_date', 'end_date')
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


class WorkExperienceAdmin(admin.ModelAdmin):
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


class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'proficiency_level', 'is_visible', 'order')
    list_filter = ('category', 'is_visible')
    search_fields = ('name',)
    list_editable = ('is_visible', 'order', 'proficiency_level')
    ordering = ('category', 'order', 'name')
    list_per_page = 25
    
    fieldsets = (
        ('Basic Info', {
            'fields': ('name', 'category')
        }),
        ('Proficiency', {
            'fields': ('proficiency_level', 'icon')
        }),
        ('Display', {
            'fields': ('is_visible', 'order')
        }),
    )


class HomeContentAdmin(admin.ModelAdmin):
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
        if HomeContent.objects.exists():
            return False
        return super().has_add_permission(request)


class AboutContentAdmin(admin.ModelAdmin):
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
        if AboutContent.objects.exists():
            return False
        return super().has_add_permission(request)


class VisitCountAdmin(admin.ModelAdmin):
    list_display = ('count', 'last_updated')
    readonly_fields = ('last_updated',)
    
    def has_add_permission(self, request):
        if VisitCount.objects.exists():
            return False
        return super().has_add_permission(request)
    
    def has_delete_permission(self, request, obj=None):
        return False


# =============================================================================
# Contact App Admin Configuration
# =============================================================================
from contact_app.models import ContactMessage


class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'is_read', 'is_resolved', 'created_at')
    list_filter = ('is_read', 'is_resolved', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    ordering = ('-created_at',)
    list_per_page = 25
    list_editable = ('is_read', 'is_resolved')
    
    fieldsets = (
        ('Contact Info', {
            'fields': ('name', 'email')
        }),
        ('Message', {
            'fields': ('subject', 'message')
        }),
        ('Status', {
            'fields': ('is_read', 'is_resolved')
        }),
        ('Metadata', {
            'fields': ('ip_address', 'user_agent', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ('ip_address', 'user_agent', 'created_at', 'updated_at')
    
    actions = ['mark_as_read', 'mark_as_unread', 'mark_as_resolved', 'mark_as_unresolved']
    
    @admin.action(description='Mark selected messages as read')
    def mark_as_read(self, request, queryset):
        updated = queryset.update(is_read=True)
        self.message_user(request, f'{updated} message(s) marked as read.')
    
    @admin.action(description='Mark selected messages as unread')
    def mark_as_unread(self, request, queryset):
        updated = queryset.update(is_read=False)
        self.message_user(request, f'{updated} message(s) marked as unread.')
    
    @admin.action(description='Mark selected messages as resolved')
    def mark_as_resolved(self, request, queryset):
        updated = queryset.update(is_resolved=True)
        self.message_user(request, f'{updated} message(s) marked as resolved.')
    
    @admin.action(description='Mark selected messages as unresolved')
    def mark_as_unresolved(self, request, queryset):
        updated = queryset.update(is_resolved=False)
        self.message_user(request, f'{updated} message(s) marked as unresolved.')


# =============================================================================
# Register all models to the custom admin site
# =============================================================================
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(WorkExperience, WorkExperienceAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(HomeContent, HomeContentAdmin)
admin.site.register(AboutContent, AboutContentAdmin)
admin.site.register(VisitCount, VisitCountAdmin)
admin.site.register(ContactMessage, ContactMessageAdmin)

