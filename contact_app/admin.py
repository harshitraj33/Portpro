from django.contrib import admin
from .models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    """
    Admin configuration for ContactMessage model with search, filtering, and ordering.
    """
    list_display = ('name', 'email', 'subject', 'is_read', 'is_resolved', 'created_at')
    list_filter = ('is_read', 'is_resolved', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    ordering = ('-created_at',)
    list_per_page = 25
    
    # Enable quick editing of is_read and is_resolved from list view
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
    
    # Custom admin actions
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