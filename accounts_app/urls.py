from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('login/', views.LoginView.as_view(), name='admin_login'),
    path('logout/', views.AdminLogoutView.as_view(), name='admin_logout'),
    path('dashboard/', views.AdminUnifiedDashboardView.as_view(), name='admin_dashboard'),
    path('projects/', views.ProjectListView.as_view(), name='admin_projects'),
    path('projects/add/', views.ProjectCreateView.as_view(), name='admin_project_add'),
    path('projects/<int:pk>/edit/', views.ProjectUpdateView.as_view(), name='admin_project_edit'),
    path('projects/<int:pk>/delete/', views.ProjectDeleteView.as_view(), name='admin_project_delete'),
    path('experience/', views.ExperienceListView.as_view(), name='admin_experience'),
    path('experience/add/', views.ExperienceCreateView.as_view(), name='admin_experience_add'),
    path('experience/<int:pk>/edit/', views.ExperienceUpdateView.as_view(), name='admin_experience_edit'),
    path('experience/<int:pk>/delete/', views.ExperienceDeleteView.as_view(), name='admin_experience_delete'),
    path('skills/', views.SkillListView.as_view(), name='admin_skills'),
    path('skills/add/', views.SkillCreateView.as_view(), name='admin_skill_add'),
    path('skills/<int:pk>/edit/', views.SkillUpdateView.as_view(), name='admin_skill_edit'),
    path('skills/<int:pk>/delete/', views.SkillDeleteView.as_view(), name='admin_skill_delete'),
    path('home-content/edit/', views.HomeContentEditView.as_view(), name='admin_home_content_edit'),
    path('messages/<int:pk>/mark-read/', views.MarkMessageAsReadView.as_view(), name='admin_message_mark_read'),
    path('messages/<int:pk>/mark-unread/', views.MarkMessageAsUnreadView.as_view(), name='admin_message_mark_unread'),
]
